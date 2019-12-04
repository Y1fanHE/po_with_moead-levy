benchmarks=("hangseng" "dax" "ftse" "sp" "nikkei")

mkdir ./tmp/${benchmarks[$1-1]}
mkdir ./tmp/${benchmarks[$1-1]}/lvxm
mkdir ./tmp/${benchmarks[$1-1]}/dem
mkdir ./tmp/${benchmarks[$1-1]}/de
mkdir ./tmp/${benchmarks[$1-1]}/ga
mkdir ./tmp/${benchmarks[$1-1]}/nsga2
mkdir ./tmp/${benchmarks[$1-1]}/lvx
mkdir ./tmp/${benchmarks[$1-1]}/unif
mkdir ./tmp/${benchmarks[$1-1]}/norm

python run_lvxm.py $1 >> ./tmp/${benchmarks[$1-1]}/lvxm/igd.txt
echo Finish MOEA/D-Levy on $1

python run_dem.py $1 >> ./tmp/${benchmarks[$1-1]}/dem/igd.txt
echo Finish MOEA/D-DEM on $1

python run_de.py $1 >> ./tmp/${benchmarks[$1-1]}/de/igd.txt
echo Finish MOEA/D-DE and CONST on $1

python run_ga.py $1 >> ./tmp/${benchmarks[$1-1]}/ga/igd.txt
echo Finish MOEA/D-GA on $1

python run_nsga2.py $1 >> ./tmp/${benchmarks[$1-1]}/nsga2/igd.txt
echo Finish NSGA-II on $1

python run_lvx.py $1 >> ./tmp/${benchmarks[$1-1]}/lvx/igd.txt
echo Finish LEVY on $1

python run_norm.py $1 >> ./tmp/${benchmarks[$1-1]}/norm/igd.txt
echo Finish NORM on $1

python run_unif.py $1 >> ./tmp/${benchmarks[$1-1]}/unif/igd.txt
echo Finish UNIF on $1
