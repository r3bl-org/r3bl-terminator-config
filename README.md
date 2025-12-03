# r3bl-terminator-config

Custom configuration for [Terminator](https://gnome-terminator.readthedocs.io/en/latest/index.html), the terminal emulator for GNOME.

## Purpose

This repository contains:

1. **Custom color theme** - A dark theme with Dracula-inspired colors, featuring a dark background (`#0d1117`), pink cursor (`#ef55a9`), and a carefully selected 16-color palette.

2. **Claude Code Shortcut plugin** - A custom Terminator plugin that adds a `Shift+Enter` keyboard shortcut to send Enter to the terminal. This is useful when working with Claude Code CLI, allowing you to submit input without leaving the home row.

## Contents

```
├── config                              # Terminator configuration (theme, keybindings)
├── install.fish                        # Installation script
└── plugins/
    └── claude_code_shortcut.py         # Claude Code shortcut plugin
```

## Installation

### Quick install (fish shell)

```fish
./install.fish
```

This copies the config and plugin to `~/.config/terminator/`. Restart Terminator to apply changes.

### Manual installation

```bash
# Backup existing config
cp -r ~/.config/terminator ~/.config/terminator.bak

# Copy config file
cp config ~/.config/terminator/config

# Copy plugin
mkdir -p ~/.config/terminator/plugins
cp plugins/claude_code_shortcut.py ~/.config/terminator/plugins/

# Restart Terminator
```

### Plugin only

```bash
mkdir -p ~/.config/terminator/plugins
cp plugins/claude_code_shortcut.py ~/.config/terminator/plugins/
```

Then enable the plugin in Terminator: **Right-click → Preferences → Plugins → Enable "ClaudeCodeShortcut"**

## Theme details

| Element | Color |
|---------|-------|
| Background | `#0d1117` |
| Foreground | `#f8f8f2` |
| Cursor | `#ef55a9` |
| Font | SFMono Nerd Font Medium 12.5 |

### Palette

```
#262626 #e356a7 #276d46 #e4f34a #bc61b9 #ca6388 #5ca7b8 #efa554
#7a7a7a #ff79c6 #3aa66b #f1fa8c #bb83b9 #f77aa7 #8be9fd #ffb86c
```

## Keybindings

| Action | Shortcut |
|--------|----------|
| Split horizontal | `Alt+D` |
| Split vertical | `Alt+R` |
| Navigate up/down/left/right | `Ctrl+Shift+Arrow` |
| Next tab | `Ctrl+Tab` |
| Previous tab | `Ctrl+Shift+Tab` |
| Clear terminal | `Alt+K` |
| Claude Code Enter (plugin) | `Shift+Enter` |

## Documentation

- [Terminator Documentation](https://gnome-terminator.readthedocs.io/en/latest/index.html)

## License

MIT License - see [LICENSE](LICENSE)
