import DataManager
import discord
import asyncio
import collections


class Player(object):

    """Docstring for Player. """

    _channel: discord.VoiceChannel = None
    _queue: collections.deque = collections.deque()
    _connectionTask: asyncio.Task = None
    _loop: asyncio.BaseEventLoop = None

    def __init__(self, channel: discord.VoiceChannel):
        """TODO: to be defined.

        Args:
            channel (discord.VoiceChannel): TODO


        """
        self._channel = channel
        self._loop = asyncio.get_running_loop()

        if self._channel.is_connected():
            task = self._loop.create_task(self.disconnect())
            self._loop.run_until_complete(task)

        self.connect()

    def connect(self):
        """TODO: Docstring for connect.
        Returns: TODO

        """
        self._connectionTask = self._loop.create_task(self._channel.connect())
        self._connectionTask.add_done_callback(self.connected)
        asyncio.ensure_future(self._connectionTask)

    async def disconnect(self):
        """docstring for disconnect"""
        await self._channel.disconnect()

    def connected(self, future: asyncio.Future):
        """TODO: Docstring for connected.

        Args:
            future (asyncio.Future): TODO

        Returns: TODO

        """
        self._channel = future.result()
        self.check_queue()

    def check_queue(self):
        """TODO: Docstring for check_queue.
        Returns: TODO

        """
        # For until connected
        while not self._connectionTask.done():
            continue

        # Return if somehow not connected
        if not self._channel.is_connected():
            return

        # If sounds left in queue
        if len(self._queue) != 0:
            sound = self._queue.popleft()
            self.play_sound(sound)

        # Otherwise leave channel
        else:
            self._loop.create_task(self.disconnect())

    def add_to_queue(self, sound: str):
        """TODO: Docstring for add_to_queue.

        Args:
            sound (str): TODO

        Returns: TODO

        """
        pass

    def play_sound(self, sound: str):
        """TODO: Docstring for play_sound.

        Args:
            sound (str): TODO

        Returns: TODO

        """
        # Get path
        path = DataManager.get_sound_path(sound)

        # Play audio and check queue when audio is done
        source = discord.FFmpegOpusAudio(path)
        self._channel.play(source, after=lambda e: self.check_queue())
