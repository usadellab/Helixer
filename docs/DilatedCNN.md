# An example with the DilatedCNN model
This uses the same example data as the LSTM model,
so please generate the data (all the steps until 
using LSTMModel.py) according to the example in 
the main README.md first.

> Note, resuming training is currently bricked for
> the DilatedCNNModel.py
 
## training
```
python3 helixer/prediction/DilatedCNNModel.py \
  --data-dir example/train/ \
  --save-model-path example/best_helixer_model.h5 \
  --epochs 5
```

## predicting
```
python3 helixer/prediction/DilatedCNNModel.py  \
  --load-model-path example/best_helixer_model.h5 \
  --test-data example/test/test_data.h5 \
  --prediction-output-path example/mpusillaCCMP1545_predictions.h5
```

## eval
```
python3 helixer/prediction/DilatedCNNModel.py  \
  --load-model-path example/best_helixer_model.h5 \
  --test-data example/test/test_data.h5 --eval
```

## scores by position and gene length
`docs/binned_evaluation.ipynb` plots the output; not tested for a DilatedCNN prediction
```
mkdir -p example/binned_eval
python3 helixer/evaluation/binned_eval.py -d example/test/test_data.h5 \
  -p example/mpusillaCCMP1545_predictions.h5 -o example/binned_eval
```
