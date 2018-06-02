"""\
Pyconstruct provides a shared Jinja2 templating API with number of utilities for
building domains.

To use the available macros, simply import them from the available libraries,
e.g.::

    {% from 'globals.pmzn' import domain, solve %}
    {% from 'linear.pmzn' import linear_model %}
    {% from 'metrics.pmzn' import hamming %}


globals.pmzn
~~~~~~~~~~~~

Collection of template macros to be used to define domains for structured
classification. Implements standard procedures for handling different inference
problems.

PROBLEMS
--------
phi
    Gets x and y as data, returns a feature vector phi(x, y).
n_features
    Returns the number of features defined in the domain.
map
    Gets x as data, computes the argmax of the score w.r.t. the given model.
loss_augmented_map
    Gets x as data, computes the argmax of the score + loss.


CONSTANTS
=========
    BOOL_SET
        An integer set of boolean values {0, 1}.
    INT_SET
        A standard set of integers.
    FLOAT_SET
        A standard set of floats.


MACROS
======

    domain(
        problem, allowed=('phi', 'map', 'loss_augmented_map')
    )
        Boilerplate for domain definition.

        PARAMETERS
        ----------
        problem : str in ['phi', 'n_features', 'map', 'loss_augmented_map']
            The problem to solve. This parameter is usually passed by the Python
            domain class.
        allowed : tuple
            Allowed problems for this domain.

        USAGE
        -----
            {% call domain(problem) %}
                % Your domain definition, e.g.
                % int: x;
                % var 0 .. 10: y;
                % constraint x + y <= 10;
            {% endcall %}


    solve(
        problem, score='score', loss='loss'
    )
        Boilerplate for problem dependent solve statement.

        PARAMETERS
        ----------
        problem : str in ['phi', 'n_features', 'map', 'loss_augmented_map']
            The problem to solve. This parameter is usually passed by the Python
            domain class.
        score : str
            The score function. Default to variable name 'score'.
        loss : str
            Formula for the loss. Used in loss_augmented_map problems.

        USAGE
        -----
            {% set loss = 'some loss' %}
            {{ solve(problem, loss=loss) }}


linear.pmzn
~~~~~~~~~~~

MACROS
======

    feature_set(
        params=none, n_features_var='N_FEATURES', feature_set_var='FEATURES'
    )
        Boilerplate for feature number definition.

        PARAMETERS
        ----------
        params : dict
            Parameters of the model.
        n_feature_var : str
            The variable name of the feature array length. Default is 'N_FEATURES'.
        feature_set_var : str
            The variable name of the feature index set: Default is 'FEATURES'.

        USAGE
        -----
        Only fixed domain features:
            {% call n_features() %}
                N_FEATURE_SET_1 + N_FEATURE_SET_2 + 5
            {% endcall %}

        Only model-dependent features:
            {{ call n_features(params) }}

        Combination of both:
            {% call n_features(params) %}
                N_FEATURE_SET_1 + N_FEATURE_SET_2 + 5
            {% endcall %}

    features(
        params=none, feature_var='phi', feature_set_var='FEATURES',
        feature_type=none
    )
        Boilerplate for features definition.

        PARAMETERS
        ----------
        params : dict
            Parameters of the model.
        feature_var : str
            The variable name of the feature array. Default is 'phi'.
        feature_set_var : str
            The variable name of the feature index set: Default is 'FEATURES'.
        feature_type : str
            The type of the features. Default is FLOAT_SET.

        USAGE
        -----
        Only fixed domain features:
            {% call features() %}
                % Your features definition, e.g.
                % [ feature1, feature2 ] ++ [ feature3 ]
            {% endcall %}

        Only model-dependent features:
            {{ call features(params) }}

        Combination of both:
            {% call features(params) %}
                % Your features definition, e.g.
                % [ feature1, feature2 ] ++ [ feature3 ]
            {% endcall %}


    linear_model(
        problem, params=none, n_features=none, n_features_var='N_FEATURES',
        feature_var='phi', feature_set_var='FEATURES', feature_type=none,
        discretize=False, factor=100, score_var='score',
        allowed=('phi', 'map', 'loss_augmented_map')
    )
        Boilerplate for defining a linear model.

        PARAMETERS
        ----------
        problem : str in ['phi', 'n_features', 'map', 'loss_augmented_map']
            The problem to solve. This parameter is usually passed by the Python
            domain class.
        params : dict
            Parameters of the model.
        n_features : str
            The number of feautures (or a fomula to compute it).
        n_feature_var : str
            The variable name of the feature array length. Default is 'N_FEATURES'.
        feature_var : str
            The variable name of the feature array. Default is 'phi'.
        feature_set_var : str
            The variable name of the feature index set: Default is 'FEATURES'.
        feature_type : str
            The type of the features. Default is FLOAT_SET.
        discretize : bool
        Wheter to discretize the weight vector and the scoring function. Use only
        if feature_type and loss_type are int. Default 'False'.
        factor : int
            The pre-multiplicative factor before discretization.
        score_var : str
            The variable name of the score to be used for inference (dot product
            between weights and features). Default 'score'.
        allowed : tuple
            Allowed problems for this model.

        USAGE
        -----
            {% call linear_model(problem, params, n_features='20') %}
                % Your features definition, e.g.
                % [ feature1, feature2 ] ++ [ feature3 ]
            {% endcall %}


metrics.pmzn
~~~~~~~~~~~~

MACROS
======

    hamming(
        sequence_set='SEQUENCE', sequence='sequence', true_sequence='true_sequence'
    )
        Formula for the hamming loss between two sequences.

        PARAMETERS
        ----------
        sequence_set : str
            The set to iterate over.
        sequence : str
            The name of predicted sequence.
        true_sequence : str
            The name of the true sequence.

"""
