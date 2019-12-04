if [ -d ./images ]; then
  rm -rf ./images
fi
if [ -d ./num_res ]; then
  rm -rf ./num_res
fi
if [ -d ./report ]; then
  rm -rf ./report
fi
mkdir ./images ./num_res ./report
echo "CREATED FOLDERS !"

python ./get_best.py
echo "COPIED BEST RUNTIMES !"
python ./plot.py
echo "FINISHED PLOTTING !"
rm -rf ./hangseng ./dax ./ftse ./sp ./nikkei
echo "CLEANED PLOTTING CACHED FILES !"

python compute_metric.py >> ./report/refpoint.txt
echo "FINISHED　COMNPUTING METRICS !"

python stat.py 1 >> ./report/hangseng.txt
python stat.py 2 >> ./report/dax.txt
python stat.py 3 >> ./report/ftse.txt
python stat.py 4 >> ./report/sp.txt
python stat.py 5 >> ./report/nikkei.txt
echo "FINISHED　STATISTICAL PROCESSING !"

if [ -d ./__pycache__ ]; then
  rm -rf ./__pycache__
fi
echo "FINISHED COMPILING CACHED FILES !"