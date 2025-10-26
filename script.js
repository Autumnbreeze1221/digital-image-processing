function showFilter(type) {
    const img = document.getElementById("filterImage");
    const text = document.getElementById("filterText");

    let src = "";
    let description = "";

    switch (type) {
        case "original":
            src = "images/original.png";
            description = "Gambar asli sebelum proses filtering dilakukan.";
            break;
        case "gaussian":
            src = "images/gaussian.png";
            description = "Gaussian filter menghaluskan gambar dengan meratakan intensitas piksel sekitarnya. Cocok untuk mengurangi noise.";
            break;
        case "median":
            src = "images/median.png";
            description = "Median filter mengganti nilai piksel dengan median dari area sekitar. Efektif untuk menghapus salt-and-pepper noise.";
            break;
        case "sharpen":
            src = "images/sharpen.png";
            description = "Sharpening filter menonjolkan detail dan meningkatkan kontras, membuat tepi objek lebih jelas.";
            break;
        case "laplacian":
            src = "images/laplacian.png";
            description = "Laplacian filter menyoroti perubahan intensitas tajam untuk mendeteksi tepi objek dalam gambar.";
            break;
    }

    img.style.opacity = 0;
    setTimeout(() => {
        img.src = src;
        img.style.opacity = 1;
        text.innerHTML = description;
    }, 400);
}