def update():
    yaw = trackIR.yaw
    pitch = trackIR.pitch

    deltaYaw = filters.delta(yaw)
    deltaPitch = filters.delta(pitch)

    if (scriptEnabled and (trackerToggled or trackerHold)):
        mouse.deltaX = deltaYaw * sensitivity
        mouse.deltaY = -deltaPitch * sensitivity

if starting:
    scriptEnabled = False
    trackerToggled = False
    trackerHold = False
    sensitivity = 30
    trackIR.update += update

toggleScript  = keyboard.getPressed(Key.Pause)
toggleTracker = keyboard.getPressed(Key.C)
trackerHold   = keyboard.getKeyDown(Key.LeftAlt)

if toggleScript:
    scriptEnabled = not scriptEnabled

if toggleTracker:
    trackerToggled = not trackerToggled