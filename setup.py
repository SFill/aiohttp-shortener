from pkg_resources import parse_requirements
from setuptools import find_packages, setup


module_name = 'shortener'


def load_requirements(fname: str) -> list:
    requirements = []
    with open(fname, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


setup(
    name=module_name,
    long_description=open('README.md').read(),
    platforms='all',
    python_requires='>=3.7',
    packages=find_packages(exclude=['tests']),
    install_requires=load_requirements('requirements.txt'),
    extras_require={'dev': load_requirements('requirements.dev.txt')},
    entry_points={
        'console_scripts': [
            '{0}-api = {0}.cmd:run_app'.format(module_name),
            '{0}-db = {0}.cmd:alembic_command'.format(module_name),
        ]
    },
    include_package_data=True
)
