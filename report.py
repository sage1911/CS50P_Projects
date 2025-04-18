def main():
    spacecraft = {"name":"Voyager 1", "distance":"163"}
    spacecraft.update({"orbit":"Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========
    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")}
    Orbit: {spacecraft.get("orbit", "Unknown")}

    =========
    """     

main()