import numpy as np

def calculate(list):
    if(len(list) != 9): raise ValueError("List must contain nine numbers.")

    npList = np.array(list)
    npList2d = npList.reshape(3,3)

    calculations = {"mean":[],
                    "variance":[],
                    "standard deviation":[],
                    "max":[],
                    "min":[],
                    "sum":[]
                    }

    npListMeanAxis1 = [np.mean(npList2d[:,0]),np.mean(npList2d[:,1]),np.mean(npList2d[:,2])]
    npListMeanAxis2 = [np.mean(npList2d[0,]),np.mean(npList2d[1,]),np.mean(npList2d[2,])]
    npListMeanAll = np.mean(npList)
    calculations["mean"] = [npListMeanAxis1,npListMeanAxis2, npListMeanAll]

    npListVarianceAxis1 = [np.var(npList2d[:,0]),np.var(npList2d[:,1]),np.var(npList2d[:,2])]
    npListVarianceAxis2 = [np.var(npList2d[0,]),np.var(npList2d[1,]),np.var(npList2d[2,])]
    npListVarianceAll = np.var(npList)
    calculations["variance"] = [npListVarianceAxis1,npListVarianceAxis2, npListVarianceAll]

    npListStandardDeviationAxis1 = [np.std(npList2d[:,0]),np.std(npList2d[:,1]),np.std(npList2d[:,2])]
    npListStandardDeviationAxis2 = [np.std(npList2d[0,]),np.std(npList2d[1,]),np.std(npList2d[2,])]
    npListStandardDeviationAll = np.std(npList)
    calculations["standard deviation"] = [npListStandardDeviationAxis1,npListStandardDeviationAxis2, npListStandardDeviationAll]

    npListMaxAxis1 = [np.max(npList2d[:,0]),np.max(npList2d[:,1]),np.max(npList2d[:,2])]
    npListMaxAxis2 = [np.max(npList2d[0,]),np.max(npList2d[1,]),np.max(npList2d[2,])]
    npListMaxAll = np.max(npList)
    calculations["max"] = [npListMaxAxis1,npListMaxAxis2, npListMaxAll]

    npListMinAxis1 = [np.min(npList2d[:,0]),np.min(npList2d[:,1]),np.min(npList2d[:,2])]
    npListMinAxis2 = [np.min(npList2d[0,]),np.min(npList2d[1,]),np.min(npList2d[2,])]
    npListMinAll = np.min(npList)
    calculations["min"] = [npListMinAxis1,npListMinAxis2, npListMinAll]

    npListSumAxis1 = [np.sum(npList2d[:,0]),np.sum(npList2d[:,1]),np.sum(npList2d[:,2])]
    npListSumAxis2 = [np.sum(npList2d[0,]),np.sum(npList2d[1,]),np.sum(npList2d[2,])]
    npListSumAll = np.sum(npList)
    calculations["sum"] = [npListSumAxis1,npListSumAxis2, npListSumAll]

    print(calculations)
    return calculations