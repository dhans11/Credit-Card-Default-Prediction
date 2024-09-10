# 🚩 Project Name: Credit Card Default Prediction

🙋🏻‍♂️ Project Owner: Ahmad Dani Rifai  
🏁 Date Finished: Juni 2024  
📞 Contact: [LinkedIn](https://www.linkedin.com/in/ahmad-dhani-0b8b6a22b/); [E-mail](adhani866@gmail.com)

---

## Objectives

mengevaluasi konsep Logistic Regression, SVM, dan KNN sebagai berikut:

- Mampu memperoleh data menggunakan BigQuery.

- Mampu memahami konsep Classification dengan Logistic Regression, SVM, dan KNN.

- Mampu mempersiapkan data untuk digunakan dalam model Logistic Regression, SVM, dan KNN.

- Mampu mengimplementasikan Logistic Regression, SVM, dan KNN untuk membuat prediksi.

---

## Dataset

```{attention}
Perhatikan petunjuk penggunaan dataset!
```

1. Buka [Google Cloud Platform](https://console.cloud.google.com/), masuk ke BigQuery, lalu buka tab `bigquery-public-data` atau link [berikut](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=ml_datasets&t=credit_card_default&page=table) untuk langsung menuju ke dataset.

2. Gunakan dataset `ml_datasets` dari database bernama `credit_card_default`.

3. Buatlah query dengan kriteria sebagai berikut:

   - Pilih **HANYA** kolom `limit_balance, sex, education_level, marital_status, age, pay_0, pay_2, pay_3, pay_4, pay_5, pay_6, bill_amt_1, bill_amt_2, bill_amt_3, bill_amt_4, bill_amt_5, bill_amt_6, pay_amt_1, pay_amt_2, pay_amt_3, pay_amt_4, pay_amt_5, pay_amt_6, default_payment_next_month`.

   - Pada kolom yang diambil diatas, terdapat beberapa kolom bertipe `STRING`. Pada saat pengambilan data dengan menggunakan perintah `SELECT`, lakukan konversi tipe data kolom-kolom bertipe `STRING` ke tipe numerik dengan panduan dibawah ini :
     | Kolom | Tipe Data Awal | Tipe Data Akhir |
     | --- | --- | --- |
     | `sex` | STRING | INT |
     | `education_level` | STRING | INT |
     | `marital_status` | STRING | INT |
     | `pay_5` | STRING | FLOAT |
     | `pay_6` | STRING | FLOAT |
     | `default_payment_next_month` | STRING | INT |

   - Konversi tipe data harus dilakukan dalam sintaks yang sama saat melakukan query ke Google BigQuery.

   - Kolom diatas hanya digunakan sebagai dataset awal. Silakan lakukan Feature Selection di-notebook setelah dataset dibuat.

   - Limit jumlah data menjadi sebanyak `nomor batch dikali dengan tahun lahir kalian`. ex: Batch 10 dan lahir tahun 1995, 10 x 1995 = 19950.

4. Simpan dataset dalam bentuk csv, dengan nama `P1G5_Set_1_<nama-students>.csv`.

5. Salin query yang telah dibuat di Google Cloud Platform, tulislah pada bagian atas notebook !

6. Tampilkan `10 data pertama` dan `10 data terakhir` dari dataset pada notebook !

---

## Problems

Buatlah model Classification untuk memprediksi `default_payment_next_month` menggunakan dataset yang sudah kalian simpan.

---

---

- Model Deployment :
  - Buat sebuah folder bernama `deployment` dan masukkan semua file yang berkaitan dengan deployment ke folder ini.
  - Buat sebuah file bernama `url.txt` yang berisi URL deployment.
  - Contoh bentuk isi repository dengan Model Deployment.
    ```
    ├── deployment/
    │   ├── app.py
    │   └── eda.py
    │   └── prediction.py
    │   └── model.pkl
    ├── P1G5_Set_1_Ahmad_Dani.ipynb
    ├── P1G5_Set_1_Ahmad_Dani.csv
    ├── url.txt
    └── README.md
    ```

---
