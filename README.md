# Overtime
> A temporal networks library written in Python.  
> This project was completed as part of my MSCS Degree at the University of Liverpool.  
> The accompanying dissertation can be found [here](documents/dissertation/COMP702___Dissertation___Open_Source_Temporal_Networks_Library.pdf).
> 
> Development of the library is ongoing through further projects at the University.  
> https://github.com/overtime3/overtime

## Basic Example
```python
import overtime as ot

network = ot.TemporalDiGraph('Sample Network', data=ot.CsvInput('./data/network.csv'))
network.add_node('g')
network.add_edge('f', 'h', 3)
network.details()

>>>	Graph Details: 
	Label: SampleNetwork 
	Directed: True 
	Static: False
	#Nodes: 7 
	#Edges: 15

ot.Circle(network)
ot.calculate_reachability(network, 'b')
>>> 5
```

## Extended Example (Transport For London)
> Functionality of the library is presented using data gathered from TFL's open-source API.  
> See [tfl_example.py](https://github.com/soca-git/COMP702-Temporal-Networks-Library/blob/master/tfl_example.py).

## Features
> A walkthrough of the library's features can be found in [features.md](./features.md). 

## Install
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install overtime.

```bash
# Using python 3.7.x
pip install overtime
```

Or clone this repository and install using [requirements.txt](./requirements.txt).
```bash
# Using python 3.7.x
pip install -r requirements.txt
```

## License

[MIT](https://choosealicense.com/licenses/mit/)

---
