from pymavlink import mavutil

master = mavutil.mavlink_connection('COM9', baud=115200)
master.wait_heartbeat()
master.mav.rc_channels_override_send(
    master.target_system,
    master.target_component,
    0, 0, 0, 1600, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
)