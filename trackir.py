def update():
    yaw = trackIR.yaw
    pitch = trackIR.pitch

    deltaYaw = filters.delta(yaw)
    deltaPitch = filters.delta(pitch)

    if (scriptEnabled and (trackerToggled or trackerHold)):
        mouse.deltaX = deltaYaw*multiply
        mouse.deltaY = -deltaPitch*multiply

if starting:
    enabled = False
    toggled = False
    activated = False
    multiply = 40
    trackIR.update += update

toggleScript = keyboard.getPressed(Key.Pause)
trackerToggle= keyboard.getPressed(Key.C)
trackerHold = keyboard.getKeyDown(Key.LeftAlt)

if toggleScript:
    scriptEnabled = not scriptEnabled

if toggleTracker:
    trackerToggled = not trackerToggled   