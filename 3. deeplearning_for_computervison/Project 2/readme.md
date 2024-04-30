# Chạy tensorflow bằng GPU của máy
1. Cài wsl với distribution mặc định là ubuntu-22.04
2. Cài driver NVIDIA loại studio mới nhất vào windown, restart lại máy. Kiếm tra
```bash
    nvidia-smi
```
3. Bật ubuntu lên làm theo [video](https://www.youtube.com/watch?v=VE5OiQSfPLg&list=LL&index=1&t=829s) và đọc bình luận Hoàng Võ
4. Cài Vscode và các extension cần thiết như remote-ssh, jupyter
5. Chuyển trình biên dịch sang môi trường ảo bạn cài tensorflow_gpu
6. pip install --upgrade jupyter ipywidgets hoặc conda install -c conda-forge jupyter ipywidgets
7. Cài clang 17.0.1 và bazel 6.5.0
- clang: https://github.com/llvm/llvm-project/releases/download/llvmorg-17.0.6/clang+llvm-17.0.6-amd64-pc-solaris2.11.tar.xz
- bazel: https://bazel.build/install/ubuntu

9. Fix NviDIA: https://gist.github.com/zrruziev/b93e1292bf2ee39284f834ec7397ee9f
https://gist.github.com/khansun/2ecf963c25b46f34062f477fe31ba5e0?permalink_comment_id=4618787

# Các bước quan trọng cần làm trong deep learning
1. Load Dataset về
- Kiểm tra các trường của dataset có bị thiếu không và xử lý
- Shuffer dataset để tránh sai xót dựa trên thứ tự thu thập dữ liệu
- Kiểm tra lượng dữ liệu có đủ lớn để áp dụng deep learning không
    - Thường các phải có khoảng 10k, 20k, 30k quan sát đổ lên
    - Dataset có tổng quát hóa không (có thiên vị về label nào đó không => Overfitting, Underfitting) nếu có thực hiện các biện pháp cân bằng lại dữ liệu, tái chọn mẫu hoặc sử dụng các thuật toán học máy được thiết kế cho xử lý dữ liệu thiên vị
2. Tiền xử lý
- Chia dataset thành các tập trani, val, test
- Normalization trainingset trước khi đi vào fully-connected layer (Phân phối chuẩn, hay Min-Max)
    - Thực tế việc normalization vẫn phải làm với output sau khi đi qua convolution layer
    - Với mỗi vòng lặp train ta sẽ tính được delta w = - (learning_rate)*(Đạo hàm tại quan sát x)
        - Sau khi normalization các trường của x thường sẽ rất nhỏ (trong khoảng 0-1) và các tham số w cần được huấn luyện sẽ nhỏ dẫn đến sự thay đổi của các parameter mỗi bước train sẽ nhỏ hơn => Train nhanh hơn