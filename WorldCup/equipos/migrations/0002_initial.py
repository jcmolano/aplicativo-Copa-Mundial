# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Continente'
        db.create_table(u'equipos_continente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreContinente', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'equipos', ['Continente'])

        # Adding model 'Equipo'
        db.create_table(u'equipos_equipo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('continente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipos.Continente'])),
            ('tecnico', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'equipos', ['Equipo'])

        # Adding model 'Jugador'
        db.create_table(u'equipos_jugador', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombreJugador', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('posicion', self.gf('django.db.models.fields.CharField')(default='seleccione', max_length=10)),
            ('equipoJugador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['equipos.Equipo'])),
            ('estatura', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('pieJugador', self.gf('django.db.models.fields.CharField')(default='seleccione', max_length=10)),
            ('tarjetaAmarilla', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('tarjetaroja', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('lesionado', self.gf('django.db.models.fields.CharField')(default='seleccione', max_length=10)),
            ('titular', self.gf('django.db.models.fields.CharField')(default='seleccione', max_length=10)),
            ('goles', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'equipos', ['Jugador'])


    def backwards(self, orm):
        # Deleting model 'Continente'
        db.delete_table(u'equipos_continente')

        # Deleting model 'Equipo'
        db.delete_table(u'equipos_equipo')

        # Deleting model 'Jugador'
        db.delete_table(u'equipos_jugador')


    models = {
        u'equipos.continente': {
            'Meta': {'object_name': 'Continente'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombreContinente': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'equipos.equipo': {
            'Meta': {'object_name': 'Equipo'},
            'continente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['equipos.Continente']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tecnico': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'equipos.jugador': {
            'Meta': {'object_name': 'Jugador'},
            'equipoJugador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['equipos.Equipo']"}),
            'estatura': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'goles': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lesionado': ('django.db.models.fields.CharField', [], {'default': "'seleccione'", 'max_length': '10'}),
            'nombreJugador': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pieJugador': ('django.db.models.fields.CharField', [], {'default': "'seleccione'", 'max_length': '10'}),
            'posicion': ('django.db.models.fields.CharField', [], {'default': "'seleccione'", 'max_length': '10'}),
            'tarjetaAmarilla': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'tarjetaroja': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'titular': ('django.db.models.fields.CharField', [], {'default': "'seleccione'", 'max_length': '10'})
        }
    }

    complete_apps = ['equipos']