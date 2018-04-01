# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Shared resource flags for Cloud Monitoring commands."""
from googlecloudsdk.calliope.concepts import concepts
from googlecloudsdk.calliope.concepts import deps
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.core import properties


def AlertPolicyAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='policy',
      help_text='Name of the alerting policy.')


def ConditionAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='condition',
      help_text='Name of the alerting policy condition.')


def NotificationChannelAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='notification_channels',
      help_text='Name of the Notification Channel.')


def ProjectAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='project',
      help_text='The Cloud project for the {resource}. If not set, it will '
                'use the project set in properties.',
      fallthroughs=[deps.PropertyFallthrough(properties.VALUES.core.project)])


def GetAlertPolicyResourceSpec():
  return concepts.ResourceSpec(
      'monitoring.projects.alertPolicies',
      resource_name='Alert Policy',
      alertPoliciesId=AlertPolicyAttributeConfig(),
      projectsId=ProjectAttributeConfig())


def GetConditionResourceSpec():
  return concepts.ResourceSpec(
      'monitoring.projects.alertPolicies.conditions',
      resource_name='condition',
      conditionsId=ConditionAttributeConfig(),
      alertPoliciesId=AlertPolicyAttributeConfig(),
      projectsId=ProjectAttributeConfig())


def GetNotificationChannelResourceSpec():
  return concepts.ResourceSpec(
      'monitoring.projects.notificationChannels',
      resource_name='Notification Channel',
      notificationChannelsId=NotificationChannelAttributeConfig(),
      projectsId=ProjectAttributeConfig())


def CreateAlertPolicyResourceArg(verb, positional=True):
  if positional:
    name = 'name'
  else:
    name = '--policy'
  help_text = 'Name of the Alert Policy ' + verb

  return concept_parsers.ResourcePresentationSpec(
      name,
      GetAlertPolicyResourceSpec(),
      help_text,
      required=True)


def CreateConditionResourceArg(verb):
  help_text = 'The name of the Condition to {}.'.format(verb)
  return concept_parsers.ResourcePresentationSpec(
      'condition',
      GetConditionResourceSpec(),
      help_text,
      required=True,
      prefixes=False)


def CreateNotificationChannelResourceArg(arg_name, extra_help, required=True,
                                         plural=False):
  """Create a resource argument for a Cloud Monitoring Notification Channel.

  Args:
    arg_name: str, the name for the arg.
    extra_help: str, the extra_help to describe the resource. This should start
      with the verb, such as 'to update', that is acting on the resource.
    required: bool, if the arg is required.
    plural: bool, if True, use a resource argument that returns a list.

  Returns:
    the PresentationSpec for the resource argument.
  """
  if plural:
    help_stem = 'Names of one or more Notification Channels '
  else:
    help_stem = 'Name of the Notification Channel '

  return concept_parsers.ResourcePresentationSpec(
      arg_name,
      GetNotificationChannelResourceSpec(),
      help_stem + extra_help,
      required=required,
      plural=plural)


def AddResourceArgs(parser, resources):
  """Add resource arguments.

  Args:
    parser: the parser for the command.
    resources: a list of resource args to add.
  """
  concept_parsers.ConceptParser(resources).AddToParser(parser)
