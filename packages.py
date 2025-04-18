class Package:
    def __init__(self, number, sender, receiver, weight):
        self.number = number
        self.sender = sender
        self.receiver = receiver
        self.weight = weight

    def __str__(self):
        return f"Package {self.number}: {self.sender} -> {self.receiver}, Weight: {self.weight}kg"
    
    def caclculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg

         



def main(): 
    packages = [
        Package(number=1, sender="Alice", receiver="Bob", weight=10),
        Package(number=2, sender="Charlie", receiver="David", weight=5)
    ]   
    for package in packages:
        print(f"{package} costs ${package.caclculate_cost(cost_per_kg=2)}")

main()    