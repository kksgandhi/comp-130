notify-send "keymaps updated"
xmodmap ~/.xmodmap
killall xcape
xcape -e 'Shift_L=BackSpace;Shift_R=Escape'
s2cctl start

