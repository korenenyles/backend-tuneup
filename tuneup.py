#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tuneup assignment"""
__author__ = "Koren Nyles, Chris Wilson, Sean Bailey"
import cProfile
import timeit
import pstats


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    def wrapper(*args, **kwargs):
        profile_obj = cProfile.Profile()
        profile_obj.enable()
        result = func(*args, **kwargs)
        profile_obj.disable()
        pstats.Stats(profile_obj).strip_dirs().sort_stats(
            'cumulative').print_stats()
        return result
    return wrapper


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie == title:
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as movies:
        movies = sorted(movies.read().splitlines())
    dupes = []
    prev_name = ""
    for movie in sorted(movies):
        if prev_name == movie:
            dupes.append(movie)
        prev_name = movie
    return dupes


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(
        stmt="""find_duplicate_movies("movies.txt")""",
        setup="""from __main__ import find_duplicate_movies"""
        )
    runtime = t.repeat(repeat=7, number=3)
    # average_runtime = sum(runtime) / len(runtime)
    return ("From timeit_helper, find_duplicate_movies takes an average of {} \n \
seconds to run.".format(min(runtime)/3))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print(timeit_helper())
    print('Found {} duplicate movies: \n{}'.format(
        len(result), "\n".join(result)))


if __name__ == '__main__':
    main()
