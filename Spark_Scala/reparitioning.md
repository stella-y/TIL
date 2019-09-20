19. 성능 튜닝
- 간접적 성능 향상 : 속성값 설정, 런타임 환경 변경
- 직접적 성능 향상 : 개별 스파크 잡, 스테이지, 태스크 성능 튜닝을 시도하거나 코드 설계를 변경해 직접적으로 성능 높이기
1. 직접적 성능 향상
    - ~~특정 스테이지나 스파크 잡이 가진 문제점에 대한 '임시방편'용 해결책~~
    - 스테이지나 잡을 개별적으로 검사하고 최적화
    1. 병렬화
        - 특정 스테이지의 처리 속도 높일 때
        - 클러스터 코어 수에 따라 설정
            - spark.default.parallelism
                - 스파크에서 사용할 파티션의 수 설정 (기본 병렬처리 수준)
                - rdd.partition().size() 등 으로 언제든 파티션 갯수 확인도 가능
            - spark.sql.shuffle.partitions
                - transformation 중 shuffle 이 병행되는 경우가 있는데, 셔플 끝난 후 rdd partition 수를 지정하는 것
        - 스테이지에서 처리할 데이터 양이 매우 많으면 클러스터의 cpu 코어당 최소 2\~3개 task 할당
    2. 필터링
        - 데이터 소스에 필터링을 위임해서 최종 결과와 무관한 데이터를 스파크에서 읽지 않고 작업 수행
        - 최대한 이른 시점에 많은 데이터를 필터링 하는게 좋을 것
    3. 파티션 재분배, 병합
        - 파티션 재분배는 셔플을 수반하게 되지만 클러스터 전체에 걸쳐 데이터가 균등하게 분배되게 됨
        - join, cache method 호출 시 매우 유용함
        - 재분배 과정 자체는 부하를 유발하게 되지만, 전체적인 성능과 스파크 잡의 병렬성을 높일 수 있음
        - coalesce
            - 셔플 대신 동일 노드의 파티션을 하나로 합치는 coalesce 메서드를 실행해서, dataframe 이나 rdd 의 전체 파티션 수를 먼저 줄이는게 좋음
            - (일반적으로 가능한 한 적은 양의 데이터를 셔플하는게 좋음)
        - repartitioning
            - 무조건 데이터를 셔플링하게 됨


## Repartitioning and coalescing

(5.4.17), (13.5)

1. 최적화 기법 - 자주 필터링하는 컬럼을 기준으로 데이터 분할
    - 컬럼 기준으로 데이터 분할 - 클러스터 전반의 물리적 데이터 구성 제어
    - repartition method 호출 → 무조건 전체 데이터 셔플(향후에 사용할 파티션 수가 현재 파티션 수보다 많거나, 컬럼 기준으로 파티션을 만드는 경우에만 사용해야 함
    - 특정 컬럼을 기준으로 자주 필터링 한다면 자주 필터링되는 컬럼을 기준으로 파티션을 재분배 하는게 좋음
    ```scala
        // 현재 파티션 수 가져오기
        df.rdd.getNumPartitions
        // 현재 dataframe 을 5개 partition 으로 분할
        df.repartition(5)
        
        // 컬럼을 기준으로 분할
        df.repartition(col("DEST_COUNTRY_NAME")
        
        // 컬럼에서 partition 갯수도 지정
        df.repartition(5, col("DEST_COUNTRY_NAME")
    ```
    - 전체 데이터 셔플 없이 파티션을 병합하려고 한다면 coalesce 를 쓰는게 좋다
```scala
        //목적지를 기준으로 셔플 수행해서, 5개 파티션으로 나누고, 전체 데이터를 셔플 없이 병합
        df.repartition(5, col("DEST_COUNTRY_NAME")).coalesce(2)
```
2. coalesce 와 repartition 비교
    - transformation 연산 수행하다보면 최초에 설정한 partition 갯수가 맞지 않는 경우 이를 조절해야할 때가 있음
    - 비교
        - repartition - 파티션 수를 늘리거나 줄이는 것을 모두 할 수 있음
        - coalesce - 줄이는 것만 가능!
    - 이 둘을 따로 두는 이유
        - repartition - shuffle 기반으로 동작 수행
        - coalesce 는 강제로 셔플 수행하라는 옵션을 지정하지 않는 한 셔플을 사용하지 않음
        - → 필터링 등으로 데이터 수가 줄어서 파티션 수를 줄이려고 할때에는 coalesce
        - → 파티션 수를 늘여야 하는 경우에만 repartition
        - ⇒ coalesce 를 사용하면 shuffle 을 발생 시키지 않기 때문에 파티션 마다 데이터 사이즈가 다를 것이라서, repartition 했을 때와 다르게 사이즈가 뒤죽박죽일 것!

- 참고
    - [https://brocess.tistory.com/183](https://brocess.tistory.com/183)
    - [https://12bme.tistory.com/438](https://12bme.tistory.com/438)
    - 설정 항목 확인 - [https://brocess.tistory.com/186](https://brocess.tistory.com/186)