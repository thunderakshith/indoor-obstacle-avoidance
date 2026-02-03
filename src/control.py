def control_decision(obstacle_map):
    if obstacle_map.sum() > 10000:
        return "TURN LEFT"
    else:
        return "MOVE FORWARD"
