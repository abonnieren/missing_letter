def get_emoji(score, total):
    percentage = (score / total) * 100

    if 0 <= percentage <= 20:
        return "😢"  # Sad face for 0-20%
    elif 21 <= percentage <= 40:
        return "😐"  # Neutral face for 21-40%
    elif 41 <= percentage <= 60:
        return "🙂"  # Slightly happy face for 41-60%
    elif 61 <= percentage <= 80:
        return "😊"  # Happy face for 61-80%
    elif 81 <= percentage <= 100:
        return "😁"  # Very happy face for 81-100%
    else:
        return "🤔"