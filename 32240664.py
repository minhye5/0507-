def convert_p6_to_p3(input_path, output_path):
    with open(input_path, 'rb') as f:
        # 매직 넘버 읽기
        magic = f.readline().strip()
        if magic != b'P6':
            raise ValueError("This is not a P6 PPM file.")

        # 주석 있는 경우 건너뛰기
        line = f.readline()
        while line.startswith(b'#'):
            line = f.readline()

        # 가로, 세로 읽기
        width, height = map(int, line.strip().split())

        # 최대 밝기값 읽기
        max_val = int(f.readline().strip())

        # 픽셀 데이터 읽기 (RGB 바이트 연속)
        pixel_bytes = f.read()

    with open(output_path, 'w') as out:
        # P3 헤더 작성
        out.write("P3\n")
        out.write(f"{width} {height}\n")
        out.write(f"{max_val}\n")

        # RGB 바이트를 텍스트로 변환
        for i in range(0, len(pixel_bytes), 3):
            r, g, b = pixel_bytes[i], pixel_bytes[i+1], pixel_bytes[i+2]
            out.write(f"{r} {g} {b}\n")

if __name__ == "__main__":
    convert_p6_to_p3("/home/data/colorP6File.ppm", "colorP3File.ppm")

