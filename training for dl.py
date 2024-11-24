import cv2
import numpy as np
import xml.etree.cElementTree as ET

# Initialize variables
drawing = False
ix, iy = -1, -1
annotations = []  # List to store annotations (bounding boxes)
zoom_factor = 1.0  # Initial zoom factor

# Function to create a PASCAL VOC XML annotation
def create_voc_xml(filename, width, height, objects):
    annotation = ET.Element("annotation")

    folder = ET.SubElement(annotation, "folder")
    folder.text = "images"  # Specify the folder name

    filename_elem = ET.SubElement(annotation, "filename")
    filename_elem.text = filename

    size = ET.SubElement(annotation, "size")
    width_elem = ET.SubElement(size, "width")
    width_elem.text = str(width)
    height_elem = ET.SubElement(size, "height")
    height_elem.text = str(height)

    for obj in objects:
        obj_elem = ET.SubElement(annotation, "object")
        name_elem = ET.SubElement(obj_elem, "name")
        name_elem.text = "dead_tree"  # Class label (you can change this)
        bndbox = ET.SubElement(obj_elem, "bndbox")
        xmin_elem = ET.SubElement(bndbox, "xmin")
        xmin_elem.text = str(obj[0])
        ymin_elem = ET.SubElement(bndbox, "ymin")
        ymin_elem.text = str(obj[1])
        xmax_elem = ET.SubElement(bndbox, "xmax")
        xmax_elem.text = str(obj[2])
        ymax_elem = ET.SubElement(bndbox, "ymax")
        ymax_elem.text = str(obj[3])

    return ET.tostring(annotation, encoding="unicode")

# Callback function for mouse events
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, zoom_factor

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # Draw a rectangle while the mouse is moved
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow('Image', img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # When the mouse button is released, store the annotation
        annotations.append((int(ix / zoom_factor), int(iy / zoom_factor), int(x / zoom_factor), int(y / zoom_factor)))
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255,    0), 2)

# Load your TIFF image using the provided path
img = cv2.imread(r"D:\Luba\chapter3\imagery\img_2.tif", -1)  # Use -1 to load as-is, including alpha channel
img_height, img_width, _ = img.shape

# Create a window with the image
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

cv2.imshow('Image', img)

# Set the mouse callback function
cv2.setMouseCallback('Image', draw_rectangle)

while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s') or key == ord('S'):  # Press 'S' to save annotations and exit
        break
    elif key == ord('+'):  # Zoom in
        zoom_factor += 0.1
        img_zoomed = cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)
        cv2.imshow('Image', img_zoomed)
    elif key == ord('-'):  # Zoom out
        zoom_factor -= 0.1
        img_zoomed = cv2.resize(img, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_LINEAR)
        cv2.imshow('Image', img_zoomed)

# Save annotations in PASCAL VOC XML format
xml_filename = 'annotations.xml'  # Specify the XML filename
with open(xml_filename, 'w') as xml_file:
    xml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    xml_file.write(create_voc_xml('your_image.tif', img_width, img_height, annotations))

print(f'Annotations saved to {xml_filename}')

cv2.destroyAllWindows()



