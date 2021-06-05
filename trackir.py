def update():
    yaw = trackIR.yaw
    pitch = trackIR.pitch

    deltaYaw = filters.delta(yaw)
    deltaPitch = filters.delta(pitch)

    if (enabled and (toggled or activated)):
        mouse.deltaX = deltaYaw*multiply
        mouse.deltaY = -deltaPitch*multiply

if starting:
    enabled = False
    toggled = False
    activated = False
    multiply = 40
    trackIR.update += update

onOrOff = keyboard.getPressed(Key.Pause)
toggle = keyboard.getPressed(Key.C)
activated = keyboard.getKeyDown(Key.LeftAlt)

if toggle:
    toggled = not toggled
    
if onOrOff:
    enabled = not enabled