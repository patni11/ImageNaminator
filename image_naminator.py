import cv2
import sys
import os


def image_naminator(images, overlay_image):
    overlay_image = cv2.imread(overlay_image)
    if os.path.isdir(images):
        all_images = os.listdir(images)
        for each in all_images:
            final_image = image_overlay(img, overlay_image)

    elif os.path.isfile(images):
        final_image = image_overlay(images, overlay_image)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows
        exit()


def image_overlay(img, overlay_image):
    img = cv2.imread(img)
    img_height, img_width = img.shape[:2]
    # overlay_height, overlay_width = overlay_image.shape[:2]

    scale_percent = 10  # percent of original size
    new_width = int(overlay_image.shape[1] * scale_percent / 100)
    new_height = int(overlay_image.shape[0] * scale_percent / 100)
    dim = (new_height, new_width)

    # r = abs(overlay_width//overlay_height)
    # new_height = abs(0.1*img_height)
    # new_width = abs(r*new_height)
    overlay_image = cv2.resize(overlay_image, dim)
    print(img_height, img_width)
    print(new_height, new_width)

    start_x, end_x = img_width-new_width-20, img_width-20
    start_y, end_y = img_height-new_height-20, img_height-20

    print(start_x - end_x)
    print(start_y - end_y)
    print(overlay_image.shape)

    #img[start_x:end_x, start_y:end_y] = overlay_image
    cv2.imwrite('final.png', overlay_image)
    cv2.imshow('final_img', overlay_image)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(
            'You need to provide 2 input. 1 folder containting images and 1 image that need to be on top')

    image_naminator(sys.argv[1], sys.argv[2])
