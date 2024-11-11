TITLE
=====

{% set ns = namespace(depth = -3) %}
{% for k, v in sample.items() recursive %}
{% set ns.depth = ns.depth + 1 %}
{% set outer_loop = loop %}
{%- if ns.depth == -2 %}
{{ k }}:
=============
{%- elif ns.depth == -1 %}
{{ k }}:
-------------
{%- elif ns.depth == 0 %}
{{ k }}:
~~~~~~~~~~~~~
{%- else %}
{{"  " * ns.depth}}- {{ k }}:
{% endif -%}

  {% if v is string %}
{{"  " * ns.depth}}- {{ v }}

  {% elif v is mapping %}

    {{ outer_loop(v.items()) }}
  
  {% elif v is sequence %}
  {% for elt in v recursive %}
  {% set ns.depth = ns.depth + 1 %}
  {% set inner_loop = loop %}
  {% if elt is mapping %}
  {{ outer_loop(elt.items()) }}
  {% elif elt is string %}
{{"  " * ns.depth}}- {{ elt }}
  {% elif elt is sequence %}
  {{ inner_loop(elt) }}
  {% else %}
  {{ elt }}
  {% endif %}
  {% set ns.depth = ns.depth - 1 %}
  {% endfor %}
  {% else %}
{{"  " * ns.depth}}- {{ v }}
  {%- endif -%}
{% set ns.depth = ns.depth - 1 %}
{%endfor%}