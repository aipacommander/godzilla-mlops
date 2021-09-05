import io
import argparse
from google.cloud import vision
import matplotlib.pyplot as plt
import cv2
import os


def get_response(input_file):
    """
    Vision APIからのレスポンスを返す関数
    ※課金に関わる処理を含むことに注意
    """
    client = vision.ImageAnnotatorClient()
    file_name = os.path.abspath(input_file)
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.object_localization(image=image)  # 課金に関わる処理
    return response


def draw_bounding_box(img, response):
    """
    レスポンスの結果を元画像に描画する関数
    """
    img_copy = img.copy()
    h, w = img_copy.shape[:-1]
    BOX_COLOR = (0, 255, 0)
    TEXT_COLOR = (0, 0, 0)
    FONT_SCALE = 0.5
    for localized_object_annotation in response.localized_object_annotations:
        name = localized_object_annotation.name
        normalized_vertices = localized_object_annotation \
            .bounding_poly.normalized_vertices
        xmin = int(normalized_vertices[0].x * w)
        ymin = int(normalized_vertices[0].y * h)
        xmax = int(normalized_vertices[2].x * w)
        ymax = int(normalized_vertices[2].y * h)
        cv2.rectangle(img_copy, (xmin, ymin), (xmax, ymax),
                      BOX_COLOR, thickness=1, lineType=cv2.LINE_AA)
        ((text_width, text_height), _) = cv2.getTextSize(
            name, cv2.FONT_HERSHEY_SIMPLEX, FONT_SCALE, 1)
        cv2.rectangle(img_copy, (xmin, ymin - int(1.3 * text_height)),
                      (xmin + text_width, ymin), BOX_COLOR, -1)
        cv2.putText(
            img_copy,
            text=name,
            org=(xmin, ymin - int(0.3 * text_height)),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=FONT_SCALE,
            color=TEXT_COLOR,
            thickness=1,
            lineType=cv2.LINE_AA,
        )
    plt.figure(figsize=[15, 15])
    plt.axis('off')
    plt.imshow(img_copy[:, :, ::-1])
    plt.title("object detection")
    plt.savefig('2.jpg')


def main(img_path):
    response = get_response(img_path)
    img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    draw_bounding_box(img, response)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', type=str, required=True)
    args = parser.parse_args()
    main(args.img_path)
