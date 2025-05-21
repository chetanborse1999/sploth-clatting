import gdown

scene_1_folder = 'https://drive.google.com/drive/folders/15NEwMTqYZz4JFwSk6lvIcvfdREYKH_ng?usp=sharing'
scene_2_folder = 'https://drive.google.com/drive/folders/1-2dci2aocyTENRZKiMlzPytxM8R6uGiR?usp=sharing'
scene_3_folder = 'https://drive.google.com/drive/folders/10KZyCtJBQzn1r2gcKTN969i_6LdJ7CsS?usp=sharing'
scene_4_folder = 'https://drive.google.com/drive/folders/1QIXhaseIQFMjHFunm3RvLcOwF0u8OIhd?usp=sharing'
scene_5_folder = 'https://drive.google.com/drive/folders/1-VeFaUMk28eIJMJomC6pDq7UYniRq2Ze?usp=sharing'
scene_6_folder = 'https://drive.google.com/drive/folders/15Tg9vXzfM96Ye-DIww4_fM5D0i1XmFGi?usp=sharing'

# all_scenes = [scene_1_folder, scene_2_folder, scene_3_folder, scene_4_folder, scene_5_folder, scene_6_folder]
all_scenes = [scene_1_folder]
output_dir = 'dataset/'
i=1

for scene_i in all_scenes:
	try:
		file_id = scene_i[scene_i.find('folders/')+8:scene_i.find('usp=sharing')-1]
		output_i = output_dir+'scene_'+str(i)
		# print(output_i)
		gdown.download_folder(id=file_id, output=output_i)
	except KeyboardInterrupt:
		print('download failed!')
		break

