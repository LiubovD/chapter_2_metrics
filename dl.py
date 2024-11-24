import os
import xml.etree.ElementTree as ET
import tensorflow as tf

# Define paths to your dataset
data_dir = 'D:/Luba/chapter3/Python_DL'
annotations_dir = os.path.join(data_dir, 'annotations')
images_dir = os.path.join(data_dir, 'images')
output_path = 'path/to/output/tfrecord'

# Define the label map (mapping class names to integers)
label_map = {'dead_tree': 1}

def create_tf_example(xml_path, image_dir):
    # Read XML annotation file
    xml = ET.parse(xml_path).getroot()

    # Extract image information
    image_path = os.path.join(image_dir, xml.find('filename').text)
    with tf.io.gfile.GFile(image_path, 'rb') as fid:
        encoded_jpg = fid.read()

    width = int(xml.find('size/width').text)
    height = int(xml.find('size/height').text)

    filename = xml.find('filename').text
    image_format = b'jpg'

    # Initialize lists to store bounding box information
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for obj in xml.findall('object'):
        class_name = obj.find('name').text
        classes_text.append(class_name.encode('utf8'))
        classes.append(label_map[class_name])
        bbox = obj.find('bndbox')
        xmins.append(float(bbox.find('xmin').text) / width)
        xmaxs.append(float(bbox.find('xmax').text) / width)
        ymins.append(float(bbox.find('ymin').text) / height)
        ymaxs.append(float(bbox.find('ymax').text) / height)

    # Create TFExample
    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': tf.train.Feature(int64_list=tf.train.Int64List(value=[height])),
        'image/width': tf.train.Feature(int64_list=tf.train.Int64List(value=[width])),
        'image/filename': tf.train.Feature(bytes_list=tf.train.BytesList(value=[filename.encode('utf8')])),
        'image/source_id': tf.train.Feature(bytes_list=tf.train.BytesList(value=[filename.encode('utf8')])),
        'image/encoded': tf.train.Feature(bytes_list=tf.train.BytesList(value=[encoded_jpg])),
        'image/format': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_format])),
        'image/object/bbox/xmin': tf.train.Feature(float_list=tf.train.FloatList(value=xmins)),
        'image/object/bbox/xmax': tf.train.Feature(float_list=tf.train.FloatList(value=xmaxs)),
        'image/object/bbox/ymin': tf.train.Feature(float_list=tf.train.FloatList(value=ymins)),
        'image/object/bbox/ymax': tf.train.Feature(float_list=tf.train.FloatList(value=ymaxs)),
        'image/object/class/text': tf.train.Feature(bytes_list=tf.train.BytesList(value=classes_text)),
        'image/object/class/label': tf.train.Feature(int64_list=tf.train.Int64List(value=classes)),
    }))
    return tf_example

# Create TFRecord file
with tf.io.TFRecordWriter(output_path) as writer:
    # Loop through XML annotations and create TFExamples
    for xml_file in os.listdir(annotations_dir):
        if xml_file.endswith('.xml'):
            xml_path = os.path.join(annotations_dir, xml_file)
            tf_example = create_tf_example(xml_path, images_dir)
            writer.write(tf_example.SerializeToString())

print(f'Successfully created TFRecord: {output_path}')

