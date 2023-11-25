def extractor(final_result):
    # [{"1": ["work hard", "10", 90, "120"]}]
    times = []

    for item in final_result:
        for key, value in item.items():
            # Extract values and convert to appropriate types
            time = float(value[3])
            minute = int(time / 60)
            remaining_seconds = int(time % 60)

            """time_units = [("minute", minute), ("second", remaining_seconds)]
            time_units = [
                (unit, round(value)) for unit, value in time_units if value >= 1
            ]

            time_str = " ".join(
                f"{value} {unit + 's'*(value != 1)}" for unit, value in time_units
            )"""
            time_str = f"{minute:02d}:{remaining_seconds:02d}"
            times.append(time_str)

    return times


res = [
    {"1": ["work hard", "10", 90, "120"]},
    {"2": ["work hard", "10", 90, "20"]},
    {"1": ["work hard", "10", 90, "145"]},
]

time = extractor(res)
print(time)
