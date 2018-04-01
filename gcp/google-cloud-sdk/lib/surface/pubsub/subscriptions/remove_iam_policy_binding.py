# Copyright 2017 Google Inc. All Rights Reserved.
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
"""Cloud Pub/Sub subscriptions remove-iam-policy-binding command."""
from googlecloudsdk.api_lib.pubsub import subscriptions
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.iam import iam_util
from googlecloudsdk.command_lib.pubsub import resource_args


@base.ReleaseTracks(base.ReleaseTrack.BETA, base.ReleaseTrack.ALPHA)
class RemoveIamPolicyBinding(base.Command):
  """Removes an IAM policy binding for a Cloud Pub/Sub Subscription."""

  detailed_help = iam_util.GetDetailedHelpForRemoveIamPolicyBinding(
      'subscription', 'my-subscription')

  @staticmethod
  def Args(parser):
    resource_args.AddSubscriptionResourceArg(
        parser, 'to remove an IAM policy binding from.')
    iam_util.AddArgsForRemoveIamPolicyBinding(parser)

  def Run(self, args):
    client = subscriptions.SubscriptionsClient()
    subscription_ref = args.CONCEPTS.subscription.Parse()
    return client.RemoveIamPolicyBinding(subscription_ref,
                                         args.member, args.role)