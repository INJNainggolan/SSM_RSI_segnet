

import cv2
'''

for a in range(1, 6 ):
    image = cv2.imread('/home/zq/output/segnet_output/4th_segnet_epoch_30_bs_2_image_50000_delete_512512/predict/predict_test/predict{0}.png'.format(a))

    print(image)

    print(image.shape)

    #####################################
    # 其他0 黑色 0 0 0 | 0 0 0

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0] == 1:  # 植被1 RGB绿色 0 255 0
                image[i][j][0] = 0
                image[i][j][1] = 255
                image[i][j][2] = 0

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0] == 2:  # 建筑2 RGB黄色 255 255 0
                image[i][j][0] = 0
                image[i][j][1] = 255
                image[i][j][2] = 255

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0] == 3:  # 水体3 RGB蓝色 255 0 0
                image[i][j][0] = 255
                image[i][j][1] = 0
                image[i][j][2] = 0

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0] == 4:  # 道路4 RGB棕色 165 42 42
                image[i][j][0] = 42
                image[i][j][1] = 42
                image[i][j][2] = 165

    #####################################
    cv2.imwrite('/home/zq/output/segnet_output/4th_segnet_epoch_30_bs_2_image_50000_delete_512512/predict/predict_test/{0}_final.png'.format(a), image[:, :])
'''







image = cv2.imread('/Volumes/V/ubuntu_zp/Home/dataset/dataset_eCognition/4/label/4.tif')

print(image)

print(image.shape)

#####################################
# 其他0 黑色 0 0 0 | 0 0 0

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][0] == 1:  # 植被1 RGB绿色 0 255 0
            image[i][j][0] = 0
            image[i][j][1] = 255
            image[i][j][2] = 0

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][0] == 2:  # 建筑2 RGB黄色 255 255 0
            image[i][j][0] = 0
            image[i][j][1] = 255
            image[i][j][2] = 255

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][0] == 3:  # 水体3 RGB蓝色 255 0 0
            image[i][j][0] = 255
            image[i][j][1] = 0
            image[i][j][2] = 0

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if image[i][j][0] == 4:  # 道路4 RGB棕色 165 42 42
            image[i][j][0] = 42
            image[i][j][1] = 42
            image[i][j][2] = 165

#####################################
cv2.imwrite('/Volumes/V/ubuntu_zp/Home/dataset/dataset_eCognition/4/label/4-vis.tif', image[:, :])
'''



import cv2


for a in range(1, 11 ):
    image = cv2.imread('/home/zq/output/segnet_output/3rd_segnet_epoch_30_bs_2_new_image_100000/predict_eCognition_RSI/predict{0}.png'.format(a))

    print(image)

    print(image.shape)

    #####################################
    # 其他0 黑色 0 0 0 | 0 0 0

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0] == 1:  # 植被1 RGB绿色 0 255 0
                image[i][j][0] = 0
                image[i][j][1] = 255
                image[i][j][2] = 0

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0] == 2:  # 建筑2 RGB黄色 255 255 0
                image[i][j][0] = 0
                image[i][j][1] = 255
                image[i][j][2] = 255

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0] == 3:  # 水体3 RGB蓝色 255 0 0
                image[i][j][0] = 255
                image[i][j][1] = 0
                image[i][j][2] = 0

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j][0] == 4:  # 道路4 RGB棕色 165 42 42
                image[i][j][0] = 42
                image[i][j][1] = 42
                image[i][j][2] = 165

    #####################################
    cv2.imwrite('/home/zq/output/segnet_output/3rd_segnet_epoch_30_bs_2_new_image_100000/predict_eCognition_RSI/vis_predict_{0}.tif'.format(a), image[:, :])
'''