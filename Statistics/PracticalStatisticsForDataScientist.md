## 1. Exploratory data analysis

- deviation / variance / standard deviation
- mean absolute deviation (= variance)
- range
- order statistics / percentile / interquentile range
- box plot / frequency table / histogram / density plot
- mode / expected value / bar chart / pie chart
- correlation coefficient(sigma((x-x^)(y-y^))/(N-1)s_x s_y) / correlation matrix / scatter plot
- contingency table / hexagonal binning / contour plot / violin plot

## 2. Data and sample distribution

- sample / population / random sampling / stratified sampling / simple random sample / sample bias
- with replacement / without replacement / representativeness / sample bias / nonrandom
- bias(non random sample / systematic error) ≠ errors on random sampling
- selection bias : 데이터를 의식적이든 무의식적이든 선택적으로 고르는 관행, 결국 오해의 소지가 있거나 단편적인 결론을 얻게 된다)
- data snooping / vast search effect
- regression to mean
- sample statistics / data distribution / sample distribution / sample variability / central limit theorem(표본 크기가 클수록 표본분포가 정규분포)
- standard error
    - 여러 표본들로부터 얻은 표본통계량의 변량
    - s/sqrt(n)= (표본 값들의 표준편차 / sqrt(표본 크기)
    - 근데 이거 구하자고 새 샘플을 수집하는 건 일반적으로 불가능 → bootstrap으로 추정하는게 일반적
- bootstrap sample / resampling
- bootstrap
    - 방법
        1. 현재 있는 표본에서 추가적으로 표본을 복원추출
        2. 각 표본에 대한 통계량과 모델을 다시 계산
        3. 위 과정을 R 번 반복
        4. R 개의 결과를 사용하여
            1. 그것들의 표준편차(통계량의 표준 오차) 계산
            2. histogram or box plot
            3. confidence interval 가져옴
    - boostrap 반복횟수는 임의로 설정 (반복 횟수가 많을수록 표준오차나 신뢰구간에 대한 추정이 더 정확해짐)
    - decision tree - bagging
    - 모집단에서 추가적으로 표본을 뽑을 때 그 표본이 얼마나 원래 표본과 비슷한지를 알려주는 것
    - 크기 n에 따라 sample distributiondl 어떻게 달라지는지 알아보기 위한 실험을 통해, sample size를 결정하는데에도 bootstrap 사용 가능
- confidence interval / confidence level / interval endpoint
    - confidence interval witn 90 %
        - sample statistics 의 bootstrap sample distribution의 90%를 포함하는 구간
- normal distribution / error / standardize ((x-x^)/s) / z-score (개별 pt를 standardize한 결과) / standard normal distribution / QQ-plot
- long tail distribution (QQ-plot에서 낮은 값의 점들은 대각선보다 훨씬 낮고 높은 값은 선보다 훨씬 위에 위치) → 더 많은 극단값을 관찰할 가능성이 있음을 의미함
- binomial distribution(bernuli distribution) - m = np, s=np(1-p) / trial
- lambda / poisson distribution / exponential distribution


## 3. Statistical test and Significance test

- treatment / treatment group / control group / randomization(처리 적용대상을 임의로 결정) / subject(처리 적용 대상) / test statistics (검정 통계량)
- null hypothesis / alternative hypothesis / one-way test / two-way test - 보통은 one-way (p값을 한쪽으로)

### 3.3 Resampling

- permutation test
    1. 여러 그룹의 결과를 단일 데이터 집합으로 결합
    2. 그룹 A, 그룹 B에서 각 그룹과 동일한 크기의 표본 각각 무작위로 (비복원)추출 → R번 반복
    3. permutation set에서의 차이에 A, B 그룹 간 차이가 포함되는지 확인

        → 포함되지 않으면 statistically significant

- term
    - proxy variable
    - (random) permutation test = randomization test
        - 변형 → exhaustive permutation test / bootstrap permutation test
- exhaustive permutation test
    - 데이터를 무작위로 섞고 나누는 대신 실제로 나눌 수 있는 모든 가능한 조합을 찾는다 (샘플 크기가 작을때에만 실용적) - shuffling 을 많이할수록 randomization test의 결과도 이와 유사해짐
- boostrap permutation test
    - resampling with replacement

### 3.4 Statistically significancy and p-value

- 전환의 차이가 우연에 의한 것 인지 검정 (이 과정을 p-value로 대체)
    - 모든 표본정보를 하나로 합침
    - 각 그룹 크기의 표본을 섞어서 뽑고 각 그룹에서의 1의 비율 차이를 기록 → 반복
    - 이 비율 차이가 얼마나 자주 원래의 비율 차이를 넘는지 그래프로 확인
- p-value : The probability that the result from null hypothesis are as extreme as observed
- significancy test : It is used to determine if the observed effect is within the range of random variation for the null hypothesis model.

### 3.8 ANOVA test

- ANOVA (ANalysis Of VAriance)
    1. gather all data in one box
    2. resample four groups with the same size and record the average value of each group / record the variance between mean of four groups → repeat
    - The probability of the resampled variance exceeds the observed :  P-value (alpha 이하라면 유의미)
- F-statistics
    - Measure the degree to which the difference between group means deviates from what is expected in the random model.
    - based on (variance caused by residual error) and (group mean - treatment effect) : The higher this ratio, the more statistically significant it is.
- pairwise test / omnibus test / decomposition of variance / f-statistics / ss

### 3.9 Chi-square test

- chi-square statistic : sum of square of Pearson residual (관측-기대)/sqrt(기대)
    1. gather all data in one box
    2. resample four groups with the same size and record the click count
    3. calcupate the pearson residual(residual between the click count on resampled result and expected result
    - How often does this value exceed the observed value?

### 3.10 Multi-armed bandit

- epsilon-greedy algorithm
    1. Generate the random number between 0 and 1
    2. If the number exists between 0 and epsilon, flip a coin
        - If coin face : A / If coin back: B
        - If the number is larger than epsilon just select the best suggestion
- Thompson sampling

### 3.11 Test power and sample size

- Power : Probability to find a specific effect size under a specific sample condition
- term : effect size / significance level
- sample size / effect size / significance level / power
    1. 2할 타자를 위해 20개의 1과 80개의 0이 들어있는 상자 가정
    2. 원하는 효과 크기를 더해서 두번째 표본을 만든다
    3. 각 상자에서 크기 n인 bootstrap sample 추출
    4. 두 bootstrap sample 에 대해서 permutation test → repeat
    - 얼마나 자주 유의미한 차이가 나는지 발견