from typing import List  # noqa: F401

import os
import subprocess
from libqtile import bar, layout, widget, extension, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

# Initial Variables
mod = "mod4"
alt = "mod1"
terminal = "alacritty"

# Colors Variables
bg_color = "#282828"
fg_color = "#ebdbb2"
urgent_color = "#fb4934"
border_color = "#d79921"

# Font
my_font_size = 13
my_font = "Noto"

# Key-bindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([alt], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.swap_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    Key([mod, "control"], "l", lazy.layout.grow(),
        desc="Grow window"),
    Key([mod, "control"], "h", lazy.layout.shrink(),
        desc="Shrink window"),
    Key([mod], "n", lazy.layout.reset(), desc="Reset all window sizes"),

    # Lunchers
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod], 'r', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="Run: ",
        background=bg_color,
        foreground=fg_color,
        selected_background=border_color,
        selected_foreground=fg_color,
        dmenu_height=20,
        fontsize=9,
    ))),
    Key([], "F12",
        lazy.group["scratchpad"].dropdown_toggle('term'),
        desc='Dropdown terminal'),
    Key([mod], "s", lazy.spawn("slock"), desc="Lock Screen"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([alt], "F4", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Toggle floating"),

    # Volume control
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer set Master 5%+")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer set Master 5%-")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer set Master toggle")
    ),
]

# Groups
groups = (
    Group(" Web", layout='max', matches=[
          Match(wm_class=["brave-browser"])], exclusive=True, spawn="brave"),
    Group(" Dev", layout='monadtall'),
    Group(" Mail", layout='monadtall', matches=[
          Match(wm_class=["Thunderbird"])], spawn="thunderbird", exclusive=True),
    Group(" Chat", layout='monadtall', matches=[
          Match(wm_class=["slack", "telegram-desktop"])], spawn=["slack", "telegram-desktop"]),
    Group(" Music", layout='monadtall', spawn="spotify"),
    Group(" Video", layout='monadtall', matches=[
          Match(wm_class=["zoom", "vlc"])], exclusive=True),
    Group(" Pass", layout='max', matches=[
          Match(wm_class=["keepassxc"])], exclusive=True, spawn="keepassxc"),
    Group(" Extras", layout='monadtall', matches=[
          Match(wm_class=["pcmanfm", "qbittorrent"])], spawn=["pcmanfm", "qbittorrent"]),
    ScratchPad('scratchpad', [DropDown(
        'term', terminal, width=0.9, height=0.9,
        x=0.05
    )])
)

for i, group in enumerate(groups, 1):
  # Switch to another group
  keys.append(Key(["control"], str(i), lazy.group[group.name].toscreen()))
  # Send current window to another group
  keys.append(Key([alt, "shift"], str(i), lazy.window.togroup(group.name)))

# Layouts
layouts = [
    layout.Max(),
    layout.Floating(
        border_width=2,
        border_normal=bg_color,
        border_focus=border_color,
    ),
    layout.MonadTall(
        border_width=2,
        border_normal=bg_color,
        border_focus=border_color,
        margin=6,
    ),
]

# Screens and Widgets
widget_defaults = dict()
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    foreground=bg_color,
                    padding=4,
                ),
                widget.GroupBox(
                    font=my_font,
                    this_current_screen_border=border_color,
                    foreground=fg_color,
                    inactive=fg_color,
                    active=fg_color,
                    fontsize=my_font_size,
                    padding_x=4,
                    borderwidth=0,
                    highlight_method="text",
                    rounded=False,
                    urgent_alert_method="text",
                    urgent_border=urgent_color,
                ),
                widget.Sep(
                    foreground=fg_color,
                    padding=5,
                    size_percent=100,
                ),
                widget.CurrentLayout(
                    font=my_font,
                    fontsize=my_font_size,
                    foreground=border_color,
                ),
                widget.Sep(
                    foreground=fg_color,
                    padding=5,
                    size_percent=100,
                ),
                widget.WindowName(
                    font=my_font,
                    foreground=border_color,
                    fontsize=my_font_size,
                ),
                widget.Net(
                    interface="enp3s0",
                    fontsize=my_font_size,
                    foreground=fg_color,
                    format="{down}",
                    fmt=" {}",
                ),
                widget.Sep(
                    foreground=fg_color,
                    padding=4,
                    size_percent=60,
                ),
                widget.CheckUpdates(
                    fmt=" {}",
                    font=my_font,
                    foreground=fg_color,
                    colour_have_updates=fg_color,
                    colour_no_updates=fg_color,
                    fontsize=my_font_size,
                    distro="Arch",
                    display_format="{updates}",
                    no_update_string="N/A",
                    update_interval=1800,
                ),
                widget.Sep(
                    foreground=fg_color,
                    padding=4,
                    size_percent=60,
                ),
                widget.Volume(
                    fmt=" {}",
                    font=my_font,
                    foreground=fg_color,
                    fontsize=my_font_size,
                    volume_app="pavucontrol",
                ),
                widget.Sep(
                    foreground=fg_color,
                    padding=4,
                    size_percent=60,
                ),
                widget.Clock(
                    font=my_font,
                    foreground=fg_color,
                    fontsize=my_font_size,
                    format=" %A, %d %B -  %H:%M"
                ),
                widget.Sep(
                    foreground=bg_color,
                    padding=4,
                )
            ],
            20,
            background=bg_color,
            opacity=0.9,
        ),
    ),
]

# Mouse options
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Run autostart.sh at start


@hook.subscribe.startup_once
def start_once():
  home = os.path.expanduser('~/.config/qtile/autostart.sh')
  subprocess.call([home])


wmname = "QTile"
