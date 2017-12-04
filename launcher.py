from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import numpy as np
import backtrader as bt
import AgentBaseStrategy as ags

if __name__ == '__main__':                        
   
   # data
   ########################################################
    data = bt.feeds.GenericCSVData(
            dataname='/home/vit/workspace/wiener-bt/btc_data/kraken10e4.csv',
            dtformat=1, #'%Y-%m-%dT%H:%M:%S.%f',
            timeframe=bt.TimeFrame.Ticks,
            datetime=0,
            high=1,
            low=1,
            open=1,
            close=1,
            volume=2,
            openinterest=-1
        )
    cerebro = bt.Cerebro()        
    cerebro.resampledata(
    data,
    timeframe=bt.TimeFrame.Minutes,
    compression=1)
    ########################################################

    cerebro.broker.setcash(100000.0)
    cerebro.broker.setcommission(commission=0.01)
    gene = np.random.randn(8)
    cerebro.addstrategy(ags.AgentBaseStrategy, gene)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

    cerebro.plot()