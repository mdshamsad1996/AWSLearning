"""Lambda handler for custom authorization"""


def lambda_handler(event, context):
    """Lambda handler for cutom almbada authorization"""

    effect = event['authorizationToken']
    resource = event['methodArn']
    response_policy = {}

    if effect == 'allow':
        principal_id = 'allowUser'
        response_policy = gen_policy(effect, resource, principal_id)
    elif effect == 'deny':
        principal_id = 'denyUser'
        response_policy = gen_policy(effect, resource, principal_id)
    else:
        raise Exception('Unauthorized')

    return response_policy


def gen_policy(effect, resource, principal_id):
    """Generate policy document based on effect and other parameter"""

    response_policy = {}

    response_policy['principalId'] = principal_id
    context_val = {}
    context_val['key'] = 'value'

    response_policy['context'] = context_val

    policy_document = {}
    policy_document['Version'] = "2012-10-17"

    statement_doc = []

    statement_one = {}
    statement_one['Action'] = 'execute-api:Invoke'
    statement_one['Effect'] = effect
    statement_one['Resource'] = resource

    statement_doc.append(statement_one)

    policy_document['Statement'] = statement_doc
    response_policy['policyDocument'] = policy_document

    return response_policy
