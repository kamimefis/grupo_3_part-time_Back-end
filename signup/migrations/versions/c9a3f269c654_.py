"""empty message

Revision ID: c9a3f269c654
Revises: 
Create Date: 2020-11-27 21:14:28.019668

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c9a3f269c654'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('persona',
    sa.Column('id_persona', sa.Integer(), nullable=False),
    sa.Column('correo', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=25), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_persona'),
    sa.UniqueConstraint('correo'),
    sa.UniqueConstraint('username')
    )
    op.drop_index('restaurante_id', table_name='lista_de_espera')
    op.drop_table('lista_de_espera')
    op.drop_index('nombre', table_name='restaurante')
    op.drop_table('restaurante')
    op.drop_table('roles')
    op.drop_table('paginas')
    op.drop_table('relacion')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relacion',
    sa.Column('id_relacion', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id_paginas', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('rol_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_paginas'], ['paginas.id_paginas'], name='relacion_ibfk_1'),
    sa.ForeignKeyConstraint(['rol_id'], ['roles.id_roles'], name='relacion_ibfk_2'),
    sa.PrimaryKeyConstraint('id_relacion'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('paginas',
    sa.Column('id_paginas', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre_pagina', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('ruta_pagina', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id_paginas'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('roles',
    sa.Column('id_roles', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('rol', mysql.VARCHAR(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id_roles'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('restaurante',
    sa.Column('id_restaurante', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('nombre', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('cantidad_maxima', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id_restaurante'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('nombre', 'restaurante', ['nombre'], unique=True)
    op.create_table('lista_de_espera',
    sa.Column('id_lista', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('restaurante_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('numero_mesas', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('fecha', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['restaurante_id'], ['restaurante.id_restaurante'], name='lista_de_espera_ibfk_1'),
    sa.PrimaryKeyConstraint('id_lista'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('restaurante_id', 'lista_de_espera', ['restaurante_id'], unique=True)
    op.drop_table('persona')
    # ### end Alembic commands ###
