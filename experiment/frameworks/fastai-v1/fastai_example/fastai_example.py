# ClearML - Fastai example code, automatic logging the model and scalars
#
import argparse

from clearml import Task

import fastai

try:
    from fastai.vision import untar_data, URLs, ImageDataBunch, rand_pad, imagenet_stats, cnn_learner, models, accuracy
except ImportError:
    raise ImportError("FastAI version %s imported, but this example is for FastAI v1." % fastai.__version__)


def main(epochs):
    Task.init(project_name="examples", task_name="fastai v1")

    path = untar_data(URLs.MNIST_SAMPLE)

    data = ImageDataBunch.from_folder(path, ds_tfms=(rand_pad(2, 28), []), bs=64, num_workers=0)
    data.normalize(imagenet_stats)

    learn = cnn_learner(data, models.resnet18, metrics=accuracy)

    accuracy(*learn.get_preds())
    learn.fit_one_cycle(epochs, 0.01)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", default=3)
    args = parser.parse_args()
    main(args.epochs)
