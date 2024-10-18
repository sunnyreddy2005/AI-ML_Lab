# Map coloring function
def is_valid_color(graph, colors, region, color):
    # Check if neighboring regions have the same color
    for neighbor in graph[region]:
        if colors[neighbor] == color:
            return False
    return True

def color_map(graph, colors, region, available_colors):
    # Base case: if all regions are colored
    if region == len(graph):
        return True

    current_region = list(graph.keys())[region]
    
    # Try assigning each available color to the current region
    for color in available_colors:
        if is_valid_color(graph, colors, current_region, color):
            colors[current_region] = color
            
            # Recursively color the next region
            if color_map(graph, colors, region + 1, available_colors):
                return True
            
            # Backtrack if coloring fails
            colors[current_region] = None
    
    return False

def main():
    # Graph representation of a map
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'D'],
        'D': ['A', 'B', 'C', 'E'],
        'E': ['B', 'D']
    }
    
    # Initialize colors of regions with None
    colors = {region: None for region in graph}
    
    # Available colors
    available_colors = ['Red', 'Green', 'Blue', 'Yellow']
    
    if color_map(graph, colors, 0, available_colors):
        print("Map coloring possible with the following colors:")
        for region, color in colors.items():
            print(f"{region}: {color}")
    else:
        print("No valid coloring found.")

if __name__ == "__main__":
    main()
