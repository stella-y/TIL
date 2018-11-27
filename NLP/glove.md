## glove 학습시키기
* https://github.com/GradySimon/tensorflow-glove
```python
import tf_glove
model = tf_glove.GloVeModel(embedding_size=300, context_size=10)
model.fit_to_corpus(corpus)
model.train(num_epochs=100)
model.embedding_for("reddit")
#array([ 0.77469945,  0.06020461,
#        0.37193006, -0.44537717,
#        ...
#        0.29987332, -0.12688215,], dtype=float32)
model.generate_tsne()
```