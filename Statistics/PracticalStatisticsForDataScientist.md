## Exploratory data analysis

- deviation / variance / standard deviation
- mean absolute deviation (= variance)
- range
- order statistics / percentile / interquentile range
- box plot / frequency table / histogram / density plot
- mode / expected value / bar chart / pie chart
- correlation coefficient(sigma((x-x^)(y-y^))/(N-1)s_x s_y) / correlation matrix / scatter plot
- contingency table / hexagonal binning / contour plot / violin plot

## data and sample distribution

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