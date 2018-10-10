# RTR105
## **Datormācības kursa elektroniskā klade**  
**ctrl+alt+T** :jauns termināls  
**ctrl+L** :notīra ekrānu  
Q :iziet  
man ... :komandas nosaukums  
echo $0 :nosaka shell valodu  
sh -> echo $0 :nomaina no bash uz sh  
**exit** :iziet no sh  
whoami :kas es esmu  
who :kas blakus  
ctrl+alt+f1-f7 :pielēguma vieta  
pwd :mana lokācija
ls :saraksts (mapes vai faili)  
ls -l :var noteikt mape vai fails (sākas ar d vai - )  
ls - a :parāda paslēptos (tie, kas sākas ar punktu)  
ls - la :apraksts par objektiem  
ls - la = ls - al  
**history** :vēsture  
history > history_2018....txt :pārnes vēsturi uz failu  
# **3. nodarbība**  
cd Music/  
ls :kas atrodas iekš music  
.  
.. :atgriež atpakaļ  
/ :saknes apgabala apzīmējums, apvieno visu info  
cd /home/user/ :atgriž uz sākumu. vai cd, vai cd~  
mkdir Manamape/ :izveido jaunu mapi  
rmdir Manamape/ :nodzēš  
man rmdir :ja neļauj nodzēst  
man rm :parādā kā nodzēst  
rm -r Manamape/ :nodzēš  
man echo :attēlo tekstu  
echo "teksts"  
echo "teksts  
>teksts  
>teksts  
>" :parāda vairākas rindiņas  
VAI  
echo -e "teksts\nteksts\nteksts  
echo "teksts" > fails1.txt :izveido failu ar tekstu  
more fails1.txt :attēlo teksta faila saturu  
cat .....  
less ..... (dažādi režīmi)  
echo "jauns teksts" **>** fails1.txt :pārraksta  
ja grib papildināt, tad **>>**  
nano fails1.txt  
ctrl x  
y  
nomaina nosaukumu  
y :teksta redaktors  
chmod540 :maina tiesības  
**failu kopēšana**  
cp fails1.txt fails101.txt :pārsauc  
mv *1*.txt Music/ :pārceļ uz music  
**pārsaukšana**  
mv fails102.txt fails103.txt :nomaina nosaukumu  
man rm :parāda atslēgas  
history > history.... :saglabā vēsturi  
  
# **3. nodarbība**  
  
python +enter  
  
vars() :vārdnīca  
print(__builtins__.__doc__)  
a = 10  
vars() :jauns mainīgais  
a = 20  
vars() :mainās mainīgais  
a +enter :pieprasa vērtību  
b +enter :nav definēts  
b = 1.56  
vars() :parāda abas vērtības  
c = 'A'  
vars()  
print(a.__doc__) :parāda datu tipus  
a- integer  
b- float  
c- str  
a*a :parāda rezultātu*  
c*c :nevar reizināt*  
exit() :iziet no python  
  
ipython +enter : cita valoda  
  
idle & +enter  
  
options : var nomainīt burtu izmēru
-"-  
a =  
b =  
c =  
type(a) +enter :nosaka datu tipu
file -> save as :ievada nosaukumu (augšā nomainās)  
ls -l
cat ...(nosaukums)  
git clone https://github.com/madaragaile/RTR105 +enter  
ls -l  
mv ... RTR105/  
ls -l
cd RTR105/  
ls -l  
nano test_1.py  
#!/usr/bin/python  
a =  
b =  
c =  
ctrl +k nokopē  
ctrl +k iekopē  

