import cv2
import numpy as np
import argparse

def scale(img,w,h):
	img_h, img_w = img.shape[:2]
	if w == 0:
		rescale = float(img_h)/h
		w = int(float(img_w)/rescale)
	if h == 0:
		rescale = float(img_w)/w
		h = int(float(img_h)/rescale)
	return(w,h)


def img_resize(img,w,h):
	if w == 0 and h == 0:
		print("No width or height detected.")
		raise ValueError("No width or height detected.")
	if w == 0 or h == 0:
		w,h = scale(img,w,h)
	return(cv2.resize(img,(w,h),interpolation=cv2.INTER_AREA))

def main(files,w=0,h=0):
	if w==None:
		w = 0
	if h==None:
		h = 0
	if w == 0 and h == 0:
		print("No width or height detected.")
		raise ValueError("No width or height detected.")
	for f in files:
		try:
			img = cv2.imread(f)
			if w == 0 or h == 0:
				w,h = scale(img,w,h)
			img = img_resize(img,w,h)
			cv2.imwrite(f"{''.join(f.split('.')[:-1])}-{w}x{h}.{f.split('.')[-1]}",img)
			print(f"Resized {f} to {''.join(f.split('.')[:-1])}-{w}x{h}.{f.split('.')[-1]}")
		except IOError:
			print(f"{f} not accessible.")


if __name__=="__main__":
	parser = argparse.ArgumentParser(prog="img-resize",description = "Resize picture")
	parser.add_argument("filename", metavar="files or directory",
						type=str, nargs="+", help="pathname to image files")
	parser.add_argument("--w", metavar="width", type=int, help="width of new image(s)")
	parser.add_argument("--h", metavar="height", type=int, help="height of new image(s)")
	args = parser.parse_args()

	main(args.filename,args.w,args.h)
