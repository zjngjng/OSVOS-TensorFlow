import os

deepmatching =  '/media/alican/no_backup02/myproj/video_segmentation/deepmatching_1.2.1_c++/deepmatching-static'
seq_name = "car-shadow"
test_frames = sorted(os.listdir(os.path.join('DAVIS', 'JPEGImages', '480p', seq_name)))
test_imgs = [os.path.join('DAVIS', 'JPEGImages', '480p', seq_name, frame) for frame in test_frames]

for i in range(len(test_imgs)-1):
    img1 = test_imgs[i]
    img2 = test_imgs[i+1]
    basename1 = os.path.basename(img1)
    basename1 = basename1.replace('.jpg', '')
    basename2 = os.path.basename(img2)
    basename2 = basename2.replace('.jpg', '')
    match_file = os.path.join('DAVIS', 'Matches', basename1 + '_' + basename2 + '.txt')
    print(match_file)
    os.system(deepmatching + ' ' + img1 + ' ' + img2 + ' ' + '-out'  + ' ' + match_file)