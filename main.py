from PIL import Image
from PIL.ExifTags import TAGS
import os

tags = []
data = []

def extract_metas(img):
    image = Image.open(f"./images/{img}")
    exifdata = image.getexif()
    data_dict = {}
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        datam = exifdata.get(tag_id)
        tags.append(tag)
        data_dict[tag] = datam.decode() if isinstance(datam, bytes) else datam
    data.append(data_dict)

def save_csv():
    csv = open("./metas.csv", 'w')
    tags_set = set(tags)
    for tag in tags_set:
        csv.write(f"{tag}, ")
    
    csv.write("\n")

    for datam in data:
        for tag in tags_set:
            csv.write(f"{datam[tag]}, ")
        csv.write("\n")
    
    csv.close()

def main():
    imgs = os.listdir("./images/")
    for img in imgs:
        extract_metas(img)
    save_csv()
    input("Output is saved inside the 'metas.csv' file. Press any key to terminate.....")

if __name__=="__main__":
    main()