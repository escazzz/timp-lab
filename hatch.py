from PIL import Image, ImageDraw

def draw_horizontal_lines(polygon_points):
  img = Image.new("RGB", (600, 600), color="white")
  draw = ImageDraw.Draw(img)

  min_y = min(point[1] for point in polygon_points)
  max_y = max(point[1] for point in polygon_points)

  for y in range(min_y, max_y + 1):
    if any(point[1] == y for point in polygon_points):
      continue

    intersection_points = []
    for i in range(len(polygon_points)):
      p1 = polygon_points[i]
      p2 = polygon_points[(i + 1) % len(polygon_points)]

      if (p1[1] <= y <= p2[1] or p2[1] <= y <= p1[1]) and p1[0] != p2[0]:
        x = p1[0] + (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1])
        intersection_points.append((x, y))

    intersection_points = [(x, y) for x, y in intersection_points if not any(point[1] == y and point[0] == x for point in polygon_points)]

    intersection_points.sort()

    for i in range(0, len(intersection_points) - 1, 2):
      draw.line((intersection_points[i], intersection_points[i + 1]), fill=(28, 28, 28))

  img.show()

polygon_points = [(0, 0), (150, 0), (100, 200), (400, 200)]
draw_horizontal_lines(polygon_points)