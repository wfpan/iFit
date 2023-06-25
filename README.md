# Introduction
This is the replication package for our work accepted by ICSE 2023, i.e., Weifeng Pan, Xin Du, Hua Ming, Dae-Kyoo Kim, Zijiang Yang. Identifying Key Classes for Initial Software Comprehension: Can We Do It Better? in Proceedings of the 45th International Conference on Software Engineering (ICSE 2023), Melbourne, Australia, May 14-20, 2023, pp. xxxx-xxxx.

# CSN<sub>WD</sub>
This directory contains the CSN<sub>WD</sub> that we built for all the subject systems used in our experiments. There are three versions of CSN<sub>WD</sub>s according to different weighting mechanisms.

# Results
This directory contains the results obtained in the experiments. We use these results to answer the research questions.

## Results: Precision and F<sub>1</sub>
This directory contains the <i>precision</i> and <i>F<sub>1</sub></i> results of iFit and eight other approaches in the baseline. 

Because there is greater redundancy in reporting <i>Precision</i>, <i>Recall</i>, and <i>F<sub>1</sub></i> at the same times. Due to the space limitation, we do not put the <i>precision</i> and <i>F<sub>1</sub></i> results in our manuscript. The file <font color="#FF0000">reasons.pdf</font> provides a detailed description of the reason why we only reported the <i>Recall</i> results in our manuscript.

# goldset
This directory contains the <i>true key classes</i> in each subject system. We collected this data set from the literature.

# iFit_SourceCode
This directory contains the source code of the implementation of iFit.