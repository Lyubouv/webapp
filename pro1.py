import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu


st.set_page_config(page_title='Aplikasi Perhitungan Stoikiometri Dasar', page_icon=':computer:')

#sidebar
with st.sidebar :
    selected = option_menu('Aplikasi Perhitungan Stoikiometri Dasar',
                         ['Tentang Aplikasi','Stoikiometri','Perhitungan Stoikiometri Dasar','Kelompok 2'],
                           default_index= 0)
#pengenalan aplikasi
if selected==('Tentang Aplikasi'):
    st.subheader('Project Webapps Kelompok 2 :computer:')
    st.title('Selamat Datang :wave:')
    st.header('Aplikasi Perhitungan Stoikiometri Dasar')
    st.write('Aplikasi ini diperuntukkan untuk mempermudah dalam perhitungan stoikiometri yang sering ditemukan dalam perhitungan kimia dengan data yang banyak dan harus dihitung dalam waktu yang singkat. Dengan adanya perkembangan teknologi aplikasi perhitungan,maka akan sangat mempermudah pengolahan data perhitungan dilaboratorium. Dengan memanfaatkan aplikasi perhitungan maka Laboran akan lebih mudah untuk mengolah data perhitungan.   ')
    
    st.image('https://i.pinimg.com/originals/28/18/73/281873087a6561e51a9186f7430deffc.png')


    
    
#halaman stoikiometri
if selected=='Stoikiometri':
    st.title('Stoikiometri')
    st.write('Stoikiometri berasal dari kata “stoicheion” dalam bahasa Yunani yang berarti mengukur. Dalam ilmu kimia, stoikiometri adalah ilmu yang mempelajari kuantitas suatu zat dalam reaksi kimia. Zat-zat tersebut meliputi massa, jumlah mol, volume, dan jumlah partikel dan molaritas.')

    st.image('https://i.pinimg.com/originals/98/d1/53/98d153f5111d9b79dd565f822c53be55.jpg',caption= 'Rumus Dasar Perhitungan Stoikiometri')

    st.write('Stoikiometri bersandar pada hukum-hukum dasar ilmu kimia salah satunya yaitu Hukum Kekekalan Massa & Hukum Perbandingan Tetap')
    col1,col2 = st.columns(2)
    col1.write('''Hukum Kekekalan Massa
    
    "massa zat-zat sebelum dan sesudah
    sebuah reaksi adalah tetap”
    ''')
    col2.write('''Hukum Perbandingan Tetap
    
    "perbandingan massa unsur-unsur 
    dalam tiap-tiap senyawa adalah tetap"''')


    
#tab 2
if selected=='Perhitungan Stoikiometri Dasar':
    st.title ('Perhitungan Stoikiometri Dasar')
    option=st.selectbox(
    'Silahkan pilih satuan konsentrasi yang ingin dicari ',
    ('Mol (n)','Molaritas (M)','Volume (v)','Partikel'))
   
    if option=='Mol (n)':
        st.image('https://www.siswapedia.com/wp-content/uploads/2019/06/rumus-mol-4.png','rumus mencari mol')
        massa=st.number_input('Masukkan massa zat (gram)')
        mr=st.number_input('Masukkan mr larutan (gram/mol)')
        if st.button('Hitung'):
            Mol=massa/mr
            st.success(f'Mol larutan sebesar {Mol} mol')
    elif option=='Molaritas (M)':
        st.image('https://1.bp.blogspot.com/-SN9gohItE8A/XB-UqkON7FI/AAAAAAAAAlk/7TNR4tugoeUNPHiW2iJk0_uojqJ0CaIgQCEwYBhgL/s1600/rumus-menghitung-molaritas.JPG', 'rumus mencari molaritas')
        mol=st.number_input('Masukkan mol zat')
        v=st.number_input('Masukkan volume pelarut (Liter)')
        if st.button('Hitung'):
            Molaritas=mol/v
            st.success(f'Molaritas larutan sebesar {Molaritas} M (mol/Liter)')
    elif option=='Volume (v)':
        st.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhuN4ygyyrInvJSdVXxARftpI9kCpUQS8E40c9PFFhRKnXSN5Cibbl2LRGLf8q6VKpO_tIjiiHsWFI6_JHI6B-G9skTweMpdpnCz6o9LYSNskfSG-pm5496jDbu2bNkc3SVAA_kooD4Z9-_yV-4E3wQ00a2wr0hkrWlEawpVQaSAZmS5llgVt0ID3ToUw/s332/Tak%20berjudul6.jpg','rumus mencari volume')
        mol=st.number_input('Masukkan mol zat')
        if st.button('Hitung'):
            Volume=mol*22.4
            st.success(f'Volume larutan sebesar {Volume}(Liter)')
    elif option=='Partikel':
        st.image('https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgoW1ttn9ZsFeuvRRd40lLSvmTPi6TX0wOpdudB3nyZZXW4gXWxTIL8dw_7i0Ut5TDQAJGtbT3krDQXhJjC4zIZLiSajLVUcnUdhDg_9KOic9l7hqrNK2i09ts0heyP5IhCd3FKY-xSvL51U8aWfaVCr5_8Nc4C8LDLodVcHIB-JdZUmCgGQtY8cUj2Wg/s600/rr1.png','mencari rumus jumlah partikel')
        mol=st.number_input('Masukkan mol zat')
        if st.button('Hitung'):
            Partikel=mol*6.02*10**23
            st.success(f'Partikel larutan sebesar {Partikel} (partikel)')
            
            
#kelompok 2
if (selected=='Kelompok 2'):
    st.title('Kelompok 2')
    st.image('https://i.pinimg.com/originals/88/43/cb/8843cbaf3b70af10e483f22d6a84c53c.jpg')
    st.write('Oleh Kelompok 2 :')
    st.write('Abdul Nazhmi Makarim (2219023)')
    st.write('Muhammad Ihsan Aula Hikam (2219115)')
    st.write('Chandrika Raysa Mulya (2219053)')
    st.write('R Amelia Nurbani Sumarya (2219146)')
   
    
