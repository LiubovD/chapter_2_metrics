import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
import pandas as pd
from assets.treeviz import tree_print
from sklearn import tree
from sklearn.metrics import accuracy_score
# sklearn provides manipulation of training sets
# here we do train/test split
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# set up
import pandas as pd
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
import seaborn as sns

# get data
df = pd.read_csv("dataset_11_01.csv")

# create our sklearn data
X = df.drop(['OID_', 'ID_upd', 'TrMrt2ct',  'TreeMort_3', 'cnsrv_prcn', 'prcnt_fore', #omit classification items
             'def_total', 'defol_1yr', 'defol_2yr',  #omit dublicates
            'pitchpine_', 'hardwood_p',  'sand_prcnt', 'bedrockdep', 'defol_3yr' #omit zero-importance variables
             , 'oak_prcnt',
             'ord_prcnt',
             'groundwate',

             ],axis=1)
y = df['TrMrt3ct']

f,ax = plt.subplots(figsize=(6, 6))
sns.heatmap(X.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
plt.show()
plt.savefig("correlation_matrix")
