#!/usr/bin/env python3
# Terminator Plugin: Claude Code Shortcut
# GPL v2 only
#
# Plugin to add a keyboard shortcut for typing Enter
# Useful for Claude Code CLI interactions
#
# Author: Created for Claude Code users
# Installation: Copy to ~/.config/terminator/plugins/

"""claude_code_shortcut.py - Terminator Plugin to add Claude Code shortcut"""

import sys
import os

# Fix imports when testing this file directly
if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))

from gi.repository import Gtk
import terminatorlib.plugin as plugin
from terminatorlib.config import Config
from terminatorlib.util import dbg, err
from terminatorlib.terminator import Terminator

from terminatorlib.plugin import KeyBindUtil

# Plugin action and description
PluginAction = "claude_code_backslash"
PluginDescription = "Claude Code: Type Enter"

# Every plugin you want Terminator to load *must* be listed in 'AVAILABLE'
AVAILABLE = ['ClaudeCodeShortcut']


class ClaudeCodeShortcut(plugin.Plugin):
    """Add keyboard shortcut to type Enter for Claude Code"""
    capabilities = ['claude_code_shortcut']
    keyb = None
    windows = []

    def __init__(self):
        """Initialize the plugin and register keyboard shortcut"""
        dbg("ClaudeCodeShortcut: Initializing plugin")

        # Get config and setup keybindings
        config = Config()
        self.keyb = KeyBindUtil(config)

        # Register the keyboard shortcut
        # Default: Shift+Enter
        # You can customize this in the config file later
        self.keyb.bindkey_check_config(
            [PluginDescription, PluginAction, "<Shift>Return"]
        )

        # Connect to all existing windows
        self.connect_signals()

        dbg("ClaudeCodeShortcut: Plugin initialized successfully")

    def unload(self):
        """Clean up when plugin is unloaded"""
        dbg("ClaudeCodeShortcut: Unloading plugin")

        # Disconnect from all windows
        for window in self.windows:
            try:
                window.disconnect_by_func(self.on_keypress)
                dbg("ClaudeCodeShortcut: Disconnected from window")
            except Exception as e:
                dbg("ClaudeCodeShortcut: No connected signals or error: %s" % str(e))

        # Unbind the keyboard shortcut
        if self.keyb:
            self.keyb.unbindkey([PluginDescription, PluginAction, "<Shift>Return"])

        dbg("ClaudeCodeShortcut: Plugin unloaded")

    def connect_signals(self):
        """Connect key-press event to all Terminator windows"""
        terminator = Terminator()
        self.windows = terminator.get_windows()

        for window in self.windows:
            window.connect('key-press-event', self.on_keypress)
            dbg("ClaudeCodeShortcut: Connected to window")

    def on_keypress(self, widget, event):
        """Handle keyboard events and check for our shortcut"""
        # Check if this key press matches our registered action
        act = self.keyb.keyaction(event)

        if act == PluginAction:
            dbg("ClaudeCodeShortcut: Shortcut triggered!")

            # Get the currently focused terminal
            terminator = Terminator()
            current_term = terminator.last_focused_term

            if current_term:
                # Send newline to the terminal
                # Using feed_child to send the character
                text_to_send = '\n'
                current_term.vte.feed_child(text_to_send.encode('utf-8'))
                dbg("ClaudeCodeShortcut: Sent Enter to terminal")

                # Return True to indicate we handled the event
                return True
            else:
                err("ClaudeCodeShortcut: No focused terminal found")

        # Return False to allow other handlers to process the event
        return False


# For testing the plugin directly
if __name__ == '__main__':
    import gi
    gi.require_version('Gtk', '3.0')

    print("ClaudeCodeShortcut Plugin")
    print("========================")
    print("This plugin adds a keyboard shortcut to type Enter")
    print("Default keybinding: Shift+Enter")
    print("")
    print("To install:")
    print("  cp claude_code_shortcut.py ~/.config/terminator/plugins/")
    print("  # Restart Terminator")
    print("")
    print("To customize the keybinding, edit ~/.config/terminator/config")
    print("and add under [plugins]:")
    print("  [[ClaudeCodeShortcut]]")
    print("    # Add custom configuration here if needed")
